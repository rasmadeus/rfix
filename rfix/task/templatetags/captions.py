from django import template
register = template.Library()


@register.simple_tag
def header(task):
    return task.header()
