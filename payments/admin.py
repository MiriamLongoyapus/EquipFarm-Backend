from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    class Meta:
        model = Payment
        fields = '__all__'


admin.site.register(Payment, PaymentAdmin)
