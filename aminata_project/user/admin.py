from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff', 'roles')

    def get_fieldsets(self, request, obj=None):
        if obj is None:
            return super().get_fieldsets(request, obj)

        if obj.is_farmer:
            fieldsets = (
                (None, {'fields': ('username', 'phone_number')}),
                ('Personal Info', {'fields': ('first_name', 'last_name','location', 'phone_number')}),
                ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions', 'roles')}),
                ('Important dates', {'fields': ('last_login', 'date_joined')}),
            )
        elif obj.is_supplier:
            fieldsets = (
                (None, {'fields': ('username', 'password')}),
                ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'location', 'company_name', 'products_offered')}),
                ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions', 'roles')}),
                ('Important dates', {'fields': ('last_login', 'date_joined')}),
            )
        else:
            fieldsets = (
                (None, {'fields': ('username', 'password')}),
                ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'location')}),
                ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions', 'roles')}),
                ('Important dates', {'fields': ('last_login', 'date_joined')}),
            )
        return fieldsets

admin.site.register(CustomUser)

