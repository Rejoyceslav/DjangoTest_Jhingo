from django import template
from tasks.models import Task

register = template.Library()


@register.simple_tag
def update_show():
    # show_instance = Task.show_task.get(id=pk)
    # show_value = show_instance.show_task
    # return show_value

    state = "none"
    return state
