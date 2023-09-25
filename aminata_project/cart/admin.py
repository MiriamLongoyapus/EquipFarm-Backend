
from django.contrib import admin
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ( 'created_at', 'quantity', 'price', 'total_price')
    
    search_fields = ('equipment_name', 'user__username')  # Change 'product_name' to 'equipment_name__name'

admin.site.register(Cart, CartAdmin)
