from django.contrib import admin
from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'parent')
    list_filter = ('parent',)


admin.register(MenuItem, MenuItemAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
