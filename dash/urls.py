from dash.views import (IndexView, DfView, HostnameView, ExternalipView,
                   IssueView, MemoryView, WhoView, NumcpuView,
                   PsView, UsersView, WhereisView, BootView,
                   LoadavgView, BandwidthView, DnsmasqView, PingView,
                   TimeView)

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view()),
    url(r'^sh/df/$', DfView.as_view()),
    url(r'^sh/hostname/$', HostnameView.as_view()),
    url(r'^sh/ip/$', ExternalipView.as_view()),
    url(r'^sh/issue/$', IssueView.as_view()),
    url(r'^sh/mem/$', MemoryView.as_view()),
    url(r'^sh/online/$', WhoView.as_view()),
    url(r'^sh/numberofcores/$', NumcpuView.as_view()),
    url(r'^sh/loadavg/$', LoadavgView.as_view()),
    url(r'^sh/ps/$', PsView.as_view()),
    url(r'^sh/users/$', UsersView.as_view()),
    url(r'^sh/whereis/$', WhereisView.as_view()),
    url(r'^sh/boot/$', BootView.as_view()),
    url(r'^sh/bandwidth/$', BandwidthView.as_view()),
    url(r'^sh/dnsmasq-leases/$', DnsmasqView.as_view()),
    url(r'^sh/ping/$', PingView.as_view()),
    url(r'^sh/time/$', TimeView.as_view()),
]
