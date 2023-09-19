from rest_framework import serializers
from payment.models import Payment

class PaymentSerializer(serializers.ModelSerializer):
   class Meta:
       model = Payment
       fields = "__all__"
    
# def update(self, instance, validated_data):
#         instance.amount = validated_data.get('amount', instance.amount)
#         instance.save()
#         return instance