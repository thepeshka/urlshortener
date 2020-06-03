from django.contrib.admin import ModelAdmin, register
from django.utils.html import format_html

from .models import URL


@register(URL)
class URLAdminModel(ModelAdmin):
    list_display = ('__str__', 'link',)

    def link(self, obj):
        return format_html('<a href="/{0}">/{0}</a>', obj.slug)
    link.allow_tags = True
    link.short_description = 'Link'
