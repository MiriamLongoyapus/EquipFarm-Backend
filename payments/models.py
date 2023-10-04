from django.db import models
from catalogue.models import  Catalogue

class Payment(models.Model):
    equipment_name = models.ForeignKey(Catalogue, on_delete=models.CASCADE,)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    payment_option = models.CharField(
        max_length=20,
        choices=[('Rental', 'Rental'), ('HirePurchase', 'HirePurchase'), ('Buy', 'Buy')],
        null=True
    )

    def __str__(self):
        return f'Payment for {self.equipment_name}'
  