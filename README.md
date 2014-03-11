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
