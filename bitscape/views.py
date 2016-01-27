from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import etag
from django.core.urlresolver import reverse
from django.core.cache cache
from django import forms

def index(request):
    example = reverse('bitscape', kwargs={'width': 200, 'height': 200})
    context = {
        'example': request.build_absolute_url
    }
    return render(request, 'index.html', context)

# Generate and return avatar
def avatar(request, width, height):
