from django import template
from tasks.models import Task

register = template.Library()


@register.simple_tag
def update_variable(value):
    return value
