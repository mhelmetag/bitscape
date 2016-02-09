from io import BytesIO
import json

from lib.mirror import Mirror

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import etag
from django.core.urlresolvers import reverse
from django.core.cache import cache
from django import forms

# def generate_etag(request, width, height):
#     content = 'Placeholder: {0} x {1}.format(width, height)'
#     return hashlib.sha1(content.encode('utf-8')).hexdigest()

# @etag(generate_etag)
def bitscape(request, image_type, size):
    form = ImageForm({'image_type': image_type, 'image_size': image_size})
    if form.is_valid():
        image = form.serve_image()
        return HttpResponse(image, content_type='image/png')
    else:
        return HttpResponseBadRequest('Invalid Image Request')

def index(request):
    # example = reverse('mirror', kwargs={'width': 200, 'height': 200})
    # context = {
    #     'example': request.build_absolute_url(example)
    # }
    return render(request, 'index.html')

class ImageForm(forms.Form):
    """Form to validate requested placeholder image"""
    IMAGE_TYPE_CHOICES = (
        ('mirror', 'mirror')
    )

    image_type = forms.ChoiceField(IMAGE_TYPE_CHOICES)
    image_size = forms.IntegerField(min_value=40, max_value=500)

    def serve_image(self):
        """Generate an image of the requested type and return as raw bytes"""
        image_format = 'PNG'
        image_type = self.cleaned_data['image_type']
        image_size = self.cleaned_data['image_size']

        # key = '{}.{}.{}'.format(width, height, image_format)
        # content = cache.get(key)
        # if content is None:

        if image_type == "mirror":
            image = Mirror.new(image_size)

        content = BytesIO()
        image.save(content, image_format)
        content.seek(0)

        # cache.set(key, content, 60 * 60)

        return content
