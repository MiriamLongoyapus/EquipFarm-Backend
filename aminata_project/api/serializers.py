from rest_framework import serializers
from user.models import CustomUser, Supplier, Farmer  

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'location', 'password')
        extra_kwargs = {
            'password': {'write_only': True},  
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)  
        user.save()
        return user

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('user', 'company_name', 'products_offered','password')

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ('user','phone_number','location')
