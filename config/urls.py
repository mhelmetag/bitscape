from django.conf.urls import patterns, include, url

import bitscape.views

urlpatterns = patterns('',
    url(r'^$', bitscape.views.index, name='index'),
    url(r'^mirror/(?P<width>[0-9]{2,3})x(?P<height>[0-9]{2,3})$',
        bitscape.views.mirror, name='mirror')
)
