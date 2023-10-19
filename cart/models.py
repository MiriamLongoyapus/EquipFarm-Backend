from django.db import models
from django.contrib.auth.models import User
from register.models import Farmer
from catalogue.models import Catalogue

class Cart(models.Model):
    PURCHASE_CHOICES=(("buy", "Buy"),
                      ("rent", "Rent"),
                      ("hire_purchase", "Hire Purchase"))
    user = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, null=True)
    is_added=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    purchase_option = models.CharField(max_length=20, choices=PURCHASE_CHOICES, default="buy")
    
    def __str__(self):
        return f"Cart Items for {self.user.user}"

# clas CartItem(models.Model)
#     cart = models.ForeignKey(Cart, o_delete=models.CASCADE)

    




    def total_price(self):
        if self.quantity is not None and self.price is not None:
            return self.quantity * self.price
        return 0  

    @classmethod
    def calculate_total_price(cls):
        total_price = 0
        carts = cls.objects.all()
        for cart in carts:
            total_price += cart.total_price()
        return total_price

    class Meta:
        app_label = 'cart'
