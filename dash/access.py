import os
import re
import sys
import pwd
import time
import socket
import platform
import struct
import fcntl
try:
    import urllib2
except ImportError:
    import urllib.request as urllib2
import subprocess
try:
    import lsb_release
except ImportError:
    lsb_release = None
from datetime import datetime
from collections import defaultdict
import psutil
try:
    from psutil import NoSuchProcess, AccessDenied
except ImportError:
    # Compatible < 2.0.0
    from psutil._error import NoSuchProcess, AccessDenied

from dash.utils import bytes2human, to_meg
from dash.conf import dnsmasq_lease_file, ping_hosts

is_mac = False
if sys.platform == 'darwin':
    is_mac = True

check_list = ['php', 'node', 'mysql', 'vim', 'python', 'ruby', 'java',
              'apache2', 'nginx', 'openssl', 'vsftpd', 'make']


def df():
    '''disk_usage'''
    df = []
    for part in psutil.disk_partitions(all=False):
        usage = psutil.disk_usage(part.mountpoint)
        percent = str(int(usage.percent)) + '%'
        disk = [part.device, bytes2human(usage.total),
                bytes2human(usage.used), bytes2human(usage.free),
                percent, part.mountpoint]
        df.append(disk)
    return df


def hostname():
    return socket.gethostname()


def get_ip_address(ifname):
    SIOCGIFADDR = 0x8915
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockfd = sock.fileno()
    ifreq = struct.pack('16sH14s', ifname.encode('utf-8'), socket.AF_INET, b'\x00'*14)
    try:
        res = fcntl.ioctl(sockfd, SIOCGIFADDR, ifreq)
    except socket.error:
        return None
    ip = struct.unpack('16sH2x4s8x', res)[2]
    return socket.inet_ntoa(ip)


def ip():
    url = 'http://ipecho.net/plain'
    external_ip = urllib2.urlopen(url).read()
    ret = [["external ip", external_ip.decode('utf-8')]]
    for network in psutil.net_io_counters(pernic=True).keys():
        if is_mac:
            import netifaces as ni
            try:
                ret.append([network, ni.ifaddresses(network)[2][0]['addr']])
            except KeyError:
                continue
        else:
            ret.append([network, get_ip_address(network)])
    return ret


def issue():
    uname = platform.uname()[2]
    if lsb_release is not None:
        distinfo = lsb_release.get_distro_information()
        lsb = distinfo.get('DESCRIPTION', 'n/a')
    elif is_mac:
        lsb = 'OS X' + platform.mac_ver()[0]
    else:
        lsb = ' '.join(platform.dist())
    return lsb + '\n' + uname


def mem():
    phymem = psutil.virtual_memory()
    total = phymem.total
    #phymem.free + buffers + cached
    free = phymem.available
    used = total - free
    return ['Mem', to_meg(total), to_meg(used), to_meg(free)]


def numberofcores():
    return str(psutil.NUM_CPUS)


def w():
    # TODO user idle time not yet achieve
    user_idle_time = '0.00s'
    ret = []
    for u in psutil.users():
        ret.append([u.name,
                    u.host,
                    datetime.fromtimestamp(u.started).strftime("%H:%M"),
                    user_idle_time
                    ])
    return ret


def ps():
    ret = []
    for p in psutil.pids():
        try:
            p_info = psutil.Process(p)
            # If stty
            if psutil.__version__ < '2.0.0':
                isterminal = p_info.terminal
                create_time = p_info.create_time
                cmdline = p_info.cmdline
                usernmae = p_info.username
            else:
                isterminal = p_info.terminal()
                create_time = p_info.create_time()
                cmdline = p_info.cmdline()
                username = p_info.username()
            if isterminal:
                terminal = isterminal.replace('/dev/tty', '')
            else:
                terminal = '??'
            # user + system (alias cputime)
            cpu_time = (p_info.cpu_times().user +
                        p_info.cpu_times().system)
            minute = int(cpu_time / 60)
            cpu_time = str(minute) + ':' + '%.2f' % (cpu_time - minute * 60)

            ret.append([username,
                        p,
                        p_info.cpu_percent(),
                        '%.1f' % p_info.memory_percent(),
                        p_info.memory_info().vms / 1024,  # vsz
                        p_info.memory_info().rss / 1024,  # rss
                        terminal,
                        str(p_info.status),  # STAT
                        datetime.fromtimestamp(
                            create_time).strftime("%I:%M%p"),
                        cpu_time,
                        ' '.join(cmdline)
                        ])
        except (NoSuchProcess, AccessDenied):
            continue
    return ret


def users():
    ret = []
    for u in pwd.getpwall():
        if u.pw_uid <= 499:
            type = 'system'
        else:
            type = 'user'
        ret.append([type, u.pw_name, u.pw_dir])
    return ret


def whereis():
    ret = []
    # When soft install more then one
    d = defaultdict(list)
    all_available_cmd = {}
    has_installed = []
    all_path = os.environ['PATH'].split(':')
    for path in all_path:
        try:
            _, _, files = next(os.walk(path))
            all_available_cmd[path] = files
        except StopIteration:  # Maybe this PATH has not exists
            continue
    for path, cmd_list in all_available_cmd.items():
        for cmd in cmd_list:
            if cmd in check_list:
                has_installed.append(cmd)
                d[cmd].append(os.path.join(path, cmd))
    for i in d.items():
        ret.append(list(i))
    not_installed = list(set(check_list).difference(set(has_installed)))
    for n in not_installed:
        ret.append([n, 'Not Installed'])
    return ret


def boot():
    try:
        boot_time = psutil.boot_time()
    except AttributeError:
        boot_time = psutil.get_boot_time()
        # Compatible < 2.0.0
    has_boot = time.time() - boot_time
    hour = int(has_boot / 3600)
    return str(hour) + ':' + str(int((has_boot - hour * 3600) / 60))


def loadavg():
    load = os.getloadavg()
    cores = psutil.NUM_CPUS
    return list(map(lambda x: ['%.2f' % x, '%.2f' % (x * 100 / cores)], load))


def bandwidth():
    def ret_netstat():
        netstat = defaultdict(int)
        get_net_io_counters = psutil.net_io_counters(pernic=True)
        for net in get_net_io_counters:
            netstat['tx'] += get_net_io_counters[net].bytes_sent
            netstat['rx'] += get_net_io_counters[net].bytes_recv
        return netstat
    old = ret_netstat()
    time.sleep(2)
    new = ret_netstat()
    return dict(tx=(new['tx'] - old['tx'])/2, rx=(new['rx'] - old['rx'])/2)


def dnsmasq_leases():
    if os.path.exists(dnsmasq_lease_file):
        ret = []
        with open(dnsmasq_lease_file) as f:
            for line in f.readlines():
                line = line.strip()
                if line:
                    l = line.split()
                    t = datetime.fromtimestamp(
                        l[0]).strftime('%m/%d/%Y %H:%M:%S')
                    ret.append([t, l[1], l[2], l[3]])
        return ret
    else:
        return []


def ping():
    #ICMP requiring root privileges. so I can not implementation written by
    # python
    avg_regex = re.compile(b'dev =.*?/(.*?)/.*?/.*ms')
    p_cmd = None
    for i in ['/bin/ping', '/sbin/ping']:
        if os.path.exists(i):
            p_cmd = i
    if p_cmd is None:
        return []

    def ret_ping(host):
        ping = subprocess.Popen("{} -qc 2 {}".format("/sbin/ping", host),
                                stdout = subprocess.PIPE,
                                stderr = subprocess.PIPE,
                                shell = True)
        match = avg_regex.search(ping.stdout.read())
        if match:
            return match.group(1).decode('utf-8')
        else:
            return ''

    ret = []
    if os.path.exists(ping_hosts):
        with open(ping_hosts) as f:
            for host in f.readlines():
                host = host.strip('\n\t#')
                if host:
                    ret.append([host, ret_ping(host)])
    else:
        for host in ['gnu.org', 'github.com', 'www.baidu.com', 'www.google.com']:
            ret.append([host, ret_ping(host)])
    return ret


def date():
    return time.strftime('%a %b %d %H:%M:%S %Z %Y')
