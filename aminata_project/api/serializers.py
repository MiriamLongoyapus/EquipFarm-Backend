from rest_framework import serializers
# from .models import Rentals, HirePurchase, Payment
from Rental.models import Rentals
from payments.models import Payment
from Hirepurchase.models import HirePurchase
# from datetime import date 
from datetime import date 


class RentalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rentals
        fields = '__all__'

class HirePurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HirePurchase
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
