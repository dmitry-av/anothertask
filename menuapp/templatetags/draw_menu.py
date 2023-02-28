from django import template
from menuapp.models import Menu
from django.db.models import Prefetch

register = template.Library()


@register.inclusion_tag('template_tags/menu.html', takes_context=True)
def draw_menu(context, slug):
    try:
        menu = Menu.objects.prefetch_related(
            Prefetch('items__items')).get(slug=slug)
        return {'menu': menu, 'context': context}
    except Menu.DoesNotExist:
        return {'menu': '', 'context': context}
