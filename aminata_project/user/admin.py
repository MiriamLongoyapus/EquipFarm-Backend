from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Supplier, Farmer

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'location')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {
            'fields': ('phone_number', 'location'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'products_offered')

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
        list_display = ('user','phone_number','location')

