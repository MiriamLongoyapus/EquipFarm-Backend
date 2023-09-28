from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # equipment_name = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    
    

    def total_price(self):
        return self.quantity * self.price
    def calculate_total_price(cls):
        total_price = 0
        carts = cls.objects.all()
        for cart in carts:
            total_price += cart.item_total_price()
        return total_price
