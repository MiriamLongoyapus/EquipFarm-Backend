
from django.contrib import admin
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'purchase_option', 'created_at', 'quantity', 'is_added')
    
    search_fields = ('equipment_name', 'user__username')  

admin.site.register(Cart, CartAdmin)
