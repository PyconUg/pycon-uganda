from django import template
import datetime

register = template.Library()

@register.simple_tag
def current_year():
    return datetime.datetime.now().year