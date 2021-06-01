import datetime

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def invert_string(value):
    return str(value[::-1])


@register.simple_tag
def current_time():
    return datetime.datetime.now().strftime('%b %d %Y %H:%M:%S')
