from django.conf.urls import patterns, include, url

import bitscape.views

urlpatterns = patterns('',
    url(r'^$', bitscape.views.index, name='index'),
    url(r'')
)
