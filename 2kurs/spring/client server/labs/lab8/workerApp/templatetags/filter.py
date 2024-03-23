

from django import template

register = template.Library()


@register.filter('order')      
def ord(value):
    c = 0
    for i in value:
        c += 1
    return c
