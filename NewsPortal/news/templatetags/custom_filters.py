from django import template

STOP_LIST = [
    'инфекция',
    ]

register = template.Library()
@register.filter()
def censor(value):
    value = str.split(value)
    if value is STOP_LIST:
        value = value.replace(STOP_LIST, '*')
        return value




