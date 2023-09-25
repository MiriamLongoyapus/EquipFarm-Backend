

from django.contrib import admin
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'product_name', 'quantity', 'price', 'total_price')
    list_filter = ('user', 'created_at')
    search_fields = ('product_name', 'user__username')

admin.site.register(Cart, CartAdmin)