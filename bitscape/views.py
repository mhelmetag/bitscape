from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import etag
from django.core.urlresolvers import reverse
from django.core.cache import cache
from django import forms
import json

from lib.mirror import Mirror

def index(request):
    # example = reverse('mirror', kwargs={'width': 200, 'height': 200})
    # context = {
    #     'example': request.build_absolute_url(example)
    # }
    return render(request, 'index.html')

# Generate and return mirror avatar

class ImageForm(forms.Form):
    """Form to validate requested placeholder image"""

    height = forms.IntegerField(min_value=1, max_value=2000)
    width = forms.IntegerField(min_value=1, max_value=2000)

    def generate_image(self, image_format='PNG'):
        """Generate an image of the requested type and return as raw bytes"""
        height = self.cleaned_data['height']
        width = self.cleaned_data['width']
        key = '{}.{}.{}'.format(width, height, image_format)
        content = cache.get(key)
        if content is None:

            # def mirror(request, width, height):
            #     form = ImageForm({'height': height, 'width': width})
            #     if form.is_valid():
            #         image = form.generate_image()
            #         return HttpResponse(image, content_type='image/png')
            #     else:
            #         return HttpResponseBadRequest('Invalid Image Request')

            # image = Image.new('RGB', (width, height))
            # draw = ImageDraw.Draw(image)
            # text = '{} X {}'.format(width, height)
            # textwidth, textheight = draw.textsize(text)
            # if textwidth < width and textheight < height:
            #     texttop = (height - textheight) // 2
            #     textleft = (width - textwidth) // 2
            #     draw.text((textleft, texttop), text, fill=(255, 255, 255))
            # content = BytesIO()
            image.save(content, image_format)
            content.seek(0)
            cache.set(key, content, 60 * 60)
        return content
