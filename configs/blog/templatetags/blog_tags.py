from django import template
from blog.models import Category, Article

register = template.Library()


@register.simple_tag()
def get_sorters():
    sorters = {
        '-views': 'Views ⬆️',
        'views': 'Views ⬇️',
        'title': 'A - Z',
        '-title': 'Z - A',
        '-created_at': 'New products',
        'created_at': 'Old products'
    }
    return sorters
