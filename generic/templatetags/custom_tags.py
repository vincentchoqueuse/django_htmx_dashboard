import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def get_field_value(instance, field_name):
    field = getattr(instance, field_name)
    if isinstance(field, str):
        output = mark_safe(markdown.markdown(field))
    else:
        output = field
    return output

@register.simple_tag
def remove_page_param(query_dict):
    query_dict = query_dict.copy()  # Make a copy to avoid modifying the original
    if 'page' in query_dict:
        query_dict.pop('page')
    return query_dict.urlencode()


