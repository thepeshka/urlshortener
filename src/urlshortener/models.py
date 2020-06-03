from django.db.models import *
from random import choices

REF_TYPES = (
    ('header', 'Header'),
    ('js', 'JavaScript')
)


def create_slug():
    return ''.join(choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=11))


class URL(Model):
    full = URLField(max_length=255)
    slug = CharField(max_length=11, default=create_slug, unique=True)
    ref_type = CharField(max_length=6, choices=REF_TYPES, default='header')
