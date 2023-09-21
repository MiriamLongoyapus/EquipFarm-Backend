from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone_number', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')

    def get_fieldsets(self, request, obj=None):
        if obj is None:
            return super().get_fieldsets(request, obj)

        if obj.is_farmer:
            fieldsets = (
                (None, {'fields': ('username','roles')}),
                ('Personal Info', {'fields': ('first_name', 'last_name')}),
                ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
                ('Important dates', {'fields': ('last_login', 'date_joined')}),
            )
        elif obj.is_supplier:
            fieldsets = (
                (None, {'fields': ('username', 'phone_number', 'roles')}),
                ('Personal Info', {'fields': ('first_name', 'last_name', 'company_name', 'products_offered')}),
                ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
                ('Important dates', {'fields': ('last_login', 'date_joined')}),
            )
        else:
            fieldsets = (
                (None, {'fields': ('username', 'phone_number')}),
                ('Personal Info', {'fields': ('first_name', 'last_name')}),
                ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
                ('Important dates', {'fields': ('last_login', 'date_joined')}),
            )
        return fieldsets

admin.site.register(CustomUser, CustomUserAdmin)
