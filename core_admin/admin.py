from django.contrib import admin

# Register your models here.
from django.contrib.admin import AdminSite
from django.urls import path
from .views import custom_admin_view

class MyAdminSite(AdminSite):
    site_header = "Admin KOROBA"
    site_title = "KOROBA Admin"
    index_title = "Bienvenue dans l'administration KOROBA"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('custom-page/', self.admin_view(custom_admin_view), name='custom_admin_page'),
        ]
        return custom_urls + urls


admin_site = MyAdminSite(name='my_grappelli_admin')
