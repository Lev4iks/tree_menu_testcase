from django.shortcuts import render
from .models import MenuItem


def menu_view(request, menu_name):
    menu = MenuItem.objects.filter(name=menu_name).first()

    return render(request, 'menu.html', {'menu': menu})
