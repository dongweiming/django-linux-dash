from django.views.generic import TemplateView, View

from access import (df, hostname, ip, issue, mem, numberofcores, w, ps,
                    whereis, users, boot, loadavg)
from utils import json_response


class IndexView(TemplateView):
    template_name = "dash/index.html"


def base(cls, func):
    @json_response
    def get(request, *args, **kwargs):
        return func()
    return type(cls, (View, ), {'get': get})


DfView = base('DfView', df)
HostnameView = base('HostnameView', hostname)
ExternalipView = base('ExternalipView', ip)
IssueView = base('IssueView', issue)
MemoryView = base('MemoryView', mem)
WhoView = base('WhoView', w)
NumcpuView = base('NumcpuView', numberofcores)
PsView = base('PsView', ps)
WhereisView = base('WhereisView', whereis)
UsersView = base('UsersView', users)
BootView = base('BootView', boot)
LoadavgView = base('LoadavgView', loadavg)
