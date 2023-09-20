from django.contrib import admin
from django.contrib import admin
from.models import Payment


class PaymentAdmin (admin.ModelAdmin):
    list_display = ("payment_date_time", "payment_amount", "validity_period","payment_balance")

admin.site.register(Payment, PaymentAdmin) 
