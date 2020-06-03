from django.shortcuts import HttpResponsePermanentRedirect, HttpResponse
from django.template.response import TemplateResponse

from .models import URL

def redirect(request, slug):
    url = URL.objects.filter(slug=slug).first()
    if not url:
        return HttpResponse(status=404)
    if url.ref_type == 'header':
        return HttpResponsePermanentRedirect(url.full)
    return TemplateResponse(request, 'redirect.html', {"href": url.full})