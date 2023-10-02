from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Farmer, Supplier

class CustomUserAdmin(UserAdmin):
    list_display = ('first_name','last_name','phone_number', 'is_staff')
    search_fields = ('username',"last_name",)
    list_filter = ('is_staff', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username',"last_name",'phone_number', 'is_staff', 'is_active', 'role', 'groups', 'user_permissions'),
        }),
    )
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Farmer)
admin.site.register(Supplier)