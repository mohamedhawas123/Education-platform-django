from django import template


register = template.Library()


def model(obj):
    try:
        return obj._meta.model_name
    
    except AttributeError:
        return None