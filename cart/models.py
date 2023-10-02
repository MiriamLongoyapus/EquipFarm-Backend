from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=None,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)

    def total_price(self):
        return self.quantity * self.price

    @classmethod
    def calculate_total_price(cls):
        total_price = 0
        carts = cls.objects.all()
        for cart in carts:
            total_price += cart.item_total_price()
        return total_price

    class Meta:
        app_label = 'cart'
