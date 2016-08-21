from django import template
register = template.Library()


@register.simple_tag
def build_meta_tags(page):
    return page.head()
