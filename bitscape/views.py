from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import etag
from django.core.urlresolvers import reverse
from django.core.cache import cache
from django import forms
import json

def index(request):
    # example = reverse('mirror', kwargs={'width': 200, 'height': 200})
    # context = {
    #     'example': request.build_absolute_url(example)
    # }
    return render(request, 'index.html')

# Generate and return mirror avatar
def mirror(request, width, height):
    pass
