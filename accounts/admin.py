from django.contrib import admin

from accounts.models import UserModel
# Register your models here.
from core_admin.admin import admin_site


@admin.register(UserModel, site=admin_site)
class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'phone_number', 'whatsapp_number' , 'user_type' )
    list_display = ('username', 'phone_number', 'user_type', 'whatsapp_number', 'created_at', 'updated_at', 'status')
    list_filter = ('username', 'user_type', 'phone_number', 'created_at', 'updated_at')
    #exclude = ('password',)