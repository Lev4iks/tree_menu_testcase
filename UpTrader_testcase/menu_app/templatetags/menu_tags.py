from django import template
from ..models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu = MenuItem.objects.filter(name=menu_name).first()
    return render_menu(menu, request.path) if menu else ''


def render_menu(menu, current_path):
    html = '<ul>'

    for item in menu.children.all():
        html = f'{html}<li>'
        html = f'''{html}<a href="{item.url}"{'class="active"' if item.url == current_path else ""}>{item.name}</a>'''

        if item.children.exists():
            html = f'{html}{render_menu(item, current_path)}'

        html = f'{html}</li>'

    html = f'{html}</ul>'
    return html
