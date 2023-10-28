from django.contrib import admin
from django.urls import path

from menu_app.views import menu_view

urlpatterns = [
    path('menu/<str:menu_name>', menu_view, name='menu'),
    path('admin/', admin.site.urls),
]
