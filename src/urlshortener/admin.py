from django.contrib.admin import ModelAdmin, register

from .models import URL


@register(URL)
class URLAdminModel(ModelAdmin):
    list_display = ('__str__', 'link',)

    def link(self, obj):
        return '<a href="/%s">/%s</a>' % (obj.slug, obj.url_field)
    link.allow_tags = True
    link.short_description = 'Link'
