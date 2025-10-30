from django import template

register = template.Library()

@register.filter(name='split')
def split(value, arg):
    """Split a string by the given separator"""
    if value:
        return value.split(arg)
    return []

@register.filter(name='trim')
def trim(value):
    """Remove leading and trailing whitespace"""
    if value:
        return value.strip()
    return value