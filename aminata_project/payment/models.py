from django.db import models
# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
# from django.utils import timezone


class Payment(models.Model):
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date_time = models.DateTimeField()
    # CustomUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='payment_payments')  
    validity_period = models.TimeField()
    
    def __str__(self):
        return f"Payment of {self.payment_amount}"

    def clean(self):
        if self.payment_amount < 0:
            raise ValidationError("Payment amount cannot be negative.")
        if self.payment_date_time > timezone.now():
            raise ValidationError("Payment date cannot be in the future.")
