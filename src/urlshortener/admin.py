from django.contrib.admin import ModelAdmin, register

from .models import URL


@register(URL)
class URLAdminModel(ModelAdmin):
    list_display = ('__str__', 'link',)

    def link_field(self, obj):
        return '<a href="/%s">/%s</a>' % (obj.slug, obj.url_field)
    link_field.allow_tags = True
    link_field.short_description = 'Link'
