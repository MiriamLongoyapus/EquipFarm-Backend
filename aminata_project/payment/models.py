from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    transaction_id = models.CharField(max_length=255)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    validity_period = models.TimeField()