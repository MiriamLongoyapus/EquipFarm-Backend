from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment_payments')  
    validity_period = models.TimeField()
 
 