from django.conf.urls import patterns, include, url

import bitscape.views

urlpatterns = (
    url(r'^$', bitscape.views.index, name='index'),
    url(r'^bitscape/(?P<image_type>[a-z]{1,10})/(?P<image_size>[0-9]{2,3})$',
        bitscape.views.bitscape, name='bitscape')
)
