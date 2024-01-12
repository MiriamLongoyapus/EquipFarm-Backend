from django.db import models
from decimal import Decimal
from catalogue.models import Catalogue

class HirePurchase(models.Model):
    equipment_name = models.ForeignKey(Catalogue,on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    down_payment = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_balance = models.DecimalField(max_digits=10, decimal_places=2)
    installment_period = models.IntegerField() 
    date = models.DateField(auto_now_add=True)
    annually=models.IntegerField(max_length=250,null=True)
    quartely=models.IntegerField(max_length=250,null=True)
    semi=models.IntegerField(max_length=250,null=True)
    monthly=models.IntegerField(max_length=250,null=True)
    


    payment_frequency = models.CharField(
        max_length=20,
        choices=[('monthly', 'Monthly'), ('quarterly', 'Quarterly'), ('annually', 'Annually'), ('semi_annually', 'Semi-Annually')]
    )
    

   
# def calculate_installment_and_balance(self):
#     if self.payment_frequency == 'monthly':
#         installment_amount = (self.total_price - self.down_payment) / Decimal(self.installment_period)
#         self.remaining_balance = self.total_price - self.down_payment
#     elif self.payment_frequency == 'quarterly':
#         installment_amount = (self.total_price - self.down_payment) / (Decimal(self.installment_period) / Decimal(3))
#         self.remaining_balance = self.total_price - self.down_payment
#     elif self.payment_frequency == 'annually':
#         installment_amount = (self.total_price - self.down_payment) / (Decimal(self.installment_period) / Decimal(2))
#         self.remaining_balance = self.total_price - self.down_payment
#     elif self.payment_frequency == 'semi_annually':
#         installment_amount = (self.total_price - self.down_payment) / Decimal(self.installment_period)
#         self.remaining_balance = self.total_price - self.down_payment
#     else:
#         installment_amount = Decimal('0.00')
#         self.remaining_balance = Decimal('0.00')
# def calculate_installment_and_balance(self):
#     if self.payment_frequency == 'monthly':
#         installment_amount = (self.total_price - self.down_payment) / Decimal(self.installment_period)
#         self.remaining_balance = self.total_price - self.down_payment
#     elif self.payment_frequency == 'quarterly':
#         installment_amount = (self.total_price - self.down_payment) / (Decimal(self.installment_period) / Decimal(3))
#         self.remaining_balance = self.total_price - self.down_payment
#     elif self.payment_frequency == 'annually':
#         installment_amount = (self.total_price - self.down_payment) / (Decimal(self.installment_period) / Decimal(2))
#         self.remaining_balance = self.total_price - self.down_payment
#     elif self.payment_frequency == 'semi_annually':
#         installment_amount = (self.total_price - self.down_payment) / Decimal(self.installment_period)
#         self.remaining_balance = self.total_price - self.down_payment
#     else:
#         installment_amount = Decimal('0.00')
#         self.remaining_balance = Decimal('0.00')

#     return installment_amount



