from django import template
import locale

register = template.Library()

@register.filter
def currency(value):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(value, grouping=True)
