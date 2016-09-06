# -*- encoding: utf8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # urls:
    url(r'^login/$', 'usr.views.login'),
    url(r'^login/do/$', 'usr.views.login_do'),
    url(r'^logout/$', 'usr.views.logout'),

)
