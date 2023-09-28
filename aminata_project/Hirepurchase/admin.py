from django.contrib import admin
from .models import HirePurchase
# Register your models here.


class HirePurchaseAdmin(admin.ModelAdmin):
    class Meta:
        model = HirePurchase
        fields = '__all__'

admin.site.register(HirePurchase, HirePurchaseAdmin)
