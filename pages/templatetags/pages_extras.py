from django import template
from pages.models import Page
 # CREAR UN TEMPLATE TAG

register = template.Library() #librería de templates

@register.simple_tag

def get_page_list():
    pages = Page.objects.all()
    return pages