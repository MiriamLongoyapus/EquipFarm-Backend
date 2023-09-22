from django.contrib import admin

# Register your models here.

# # Register your models here.

# from django.contrib import admin
# from .models import Farmer, Supplier

# class FarmerAdmin(admin.ModelAdmin):
#     list_display = ('user','first_name','last_name','phone_number', 'location')
#     search_fields = ('first_name', 'location')

# class SupplierAdmin(admin.ModelAdmin):
#     list_display = ('user','company_name', 'first_name', 'last_name', 'phone_number')
#     search_fields = ('first_name', 'company_name')

# admin.site.register(Farmer, FarmerAdmin)
# admin.site.register(Supplier, SupplierAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Farmer, Supplier

class CustomUserAdmin(UserAdmin):
    list_display = ('first_name','last_name','phone_number', 'is_staff')
    search_fields = ('username',)
    list_filter = ('is_staff', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','phone_number', 'is_staff', 'is_active', 'role', 'groups', 'user_permissions'),
        }),
    )
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Farmer)
admin.site.register(Supplier)