from django.conf.urls import patterns
from views import (IndexView, DfView, HostnameView, ExternalipView,
                   IssueView, MemoryView, WhoView, NumcpuView,
                   PsView, UsersView, WhereisView, BootView,
                   LoadavgView,SpeedView)


urlpatterns = patterns('',
                       (r'^$', IndexView.as_view()),
                       (r'^sh/df/$', DfView.as_view()),
                       (r'^sh/hostname/$', HostnameView.as_view()),
                       (r'^sh/ip/$', ExternalipView.as_view()),
                       (r'^sh/issue/$', IssueView.as_view()),
                       (r'^sh/mem/$', MemoryView.as_view()),
                       (r'^sh/online/$', WhoView.as_view()),
                       (r'^sh/numberofcores/$', NumcpuView.as_view()),
                       (r'^sh/loadavg/$', LoadavgView.as_view()),
                       (r'^sh/ps/$', PsView.as_view()),
                       (r'^sh/users/$', UsersView.as_view()),
                       (r'^sh/whereis/$', WhereisView.as_view()),
                       (r'^sh/boot/$', BootView.as_view()),
                       (r'^sh/speed/$', SpeedView.as_view()),
                       )
