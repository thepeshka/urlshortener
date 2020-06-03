from django.contrib.admin import ModelAdmin, register

from .models import URL


@register(URL)
class URLAdminModel(ModelAdmin):
    pass
