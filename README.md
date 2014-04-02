django-linux-dash
=================

A clone of linux-dash written in Django, Most use psutils, Not use systemcall method. Also provide python3 compatible.


This is Python Django redo of [Linux-Dash](https://github.com/afaqurk/linux-dash) from Github user [afaqurk](https://github.com/afaqurk)

Installation
============

You need django>1.4 and [psutil](http://code.google.com/p/psutil/):

    $pip install/easy_install django
    $pip install/easy_install psutil

If you use OS X, also need [netifaces](https://pypi.python.org/pypi/netifaces):

    $pip install/easy_install netifaces

Run it!
====

    $git clone https://github.com/dongweiming/django-linux-dash
    $cd django-linux-dash
    $cp dash/conf{.example,}.py
    $python manage.py runserver 0.0.0.0:8000

    and open your webbrowser, and type http://localhost:8000

News
===

* [https://news.ycombinator.com/item?id=7125153](https://news.ycombinator.com/item?id=7125153)
* [http://www.linuxpromagazine.com/Online/Blogs/Productivity-Sauce/Monitor-Your-server-with-Linux-Dash](http://www.linu\
xpromagazine.com/Online/Blogs/Productivity-Sauce/Monitor-Your-server-with-Linux-Dash)
* [http://www.lafermeduweb.net/billet/linux-dash-un-dashboard-simple-pour-monitorer-votre-serveur-linux-1698.html](http\
://www.lafermeduweb.net/billet/linux-dash-un-dashboard-simple-pour-monitorer-votre-serveur-linux-1698.html)
* [http://linuxundich.de/ubuntu/linux-dash-als-alternative-zu-monitoring-mittels-phpsysinfo/](http://linuxundich.de/ubu\
ntu/linux-dash-als-alternative-zu-monitoring-mittels-phpsysinfo/)
* [http://www.html.it/articoli/monitoring-di-un-server-linux-con-linux-dash/](http://www.html.it/articoli/monitoring-di\
-un-server-linux-con-linux-dash/)
* [https://www.youtube.com/watch?v=3gb3z-a7XfA](https://www.youtube.com/watch?v=3gb3z-a7XfA)
* [http://www.ubuntugeek.com/linux-dash-a-low-overhead-monitoring-web-dashboard-for-a-gnulinux-machine.html](http://www\
.ubuntugeek.com/linux-dash-a-low-overhead-monitoring-web-dashboard-for-a-gnulinux-machine.html)
* [http://www.oschina.net/p/linux-dash](http://www.oschina.net/p/linux-dash)

## Credits:
 * [Dashboard Template](http://www.egrappler.com/templatevamp-free-twitter-bootstrap-admin-template/)
  * [Bootstrap](http://getbootstrap.com)
