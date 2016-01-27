from django.conf.urls import patterns, include, url

import bitscape.views

urlpatterns = patterns('',
    url(r'^$', bitscape.views.index, name='index'),
    url(r'^avatar/(?P<width>[0-9]{2,3})x(?P<height>[0-9]{2,3}/$',
        avatar, name='avatar')
)
