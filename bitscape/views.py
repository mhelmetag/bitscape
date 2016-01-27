from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import etag
from django.core.urlresolver import reverse
from django.core.cache cache
from django import forms

# Create your views here.
def index(request):
    example = reverse('bitscape', kwargs={'width': 200, 'height': 200})
