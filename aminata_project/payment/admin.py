from django.contrib import admin
from django.contrib import admin
from.models import Payment

class PaymentAdmin (admin.ModelAdmin):
    list_display = ("transaction_id", "user", "payment_date", "payment_amount", "validity_period")

admin.site.register(Payment, PaymentAdmin) 
