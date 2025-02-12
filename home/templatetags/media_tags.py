from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def media(file):
    return f"{settings.MEDIA_URL}{file}"
