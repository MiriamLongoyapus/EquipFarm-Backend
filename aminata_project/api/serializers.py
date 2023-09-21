from rest_framework import serializers
from django.contrib.auth import authenticate
from users.models import CustomUser, Role
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from users.models import CustomUser 



class CommonRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'phone_number', 'roles']
        
    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data.get('phone_number'))
        user.save()
        return user

class FarmerRegistrationSerializer(CommonRegistrationSerializer):
    username = serializers.CharField()
    phone_number = serializers.CharField()
    
    class Meta:
        model = CustomUser
        fields = CommonRegistrationSerializer.Meta.fields + ['phone_number']
        
    def create(self, validated_data):
        user = super().create(validated_data)
        farmer_role, _ = Role.objects.get_or_create(name="Farmer")
        user.roles.add(farmer_role)
        return user


class SupplierRegistrationSerializer(CommonRegistrationSerializer):
    username = serializers.CharField()
    company_name = serializers.CharField()
    products_offered = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = CommonRegistrationSerializer.Meta.fields + ['company_name', 'products_offered']

    def create(self, validated_data):
        user = super().create(validated_data)
        supplier_role, _ = Role.objects.get_or_create(name="Supplier")
        user.roles.add(supplier_role)
        return user



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    phone_number = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        phone_number = data.get('phone_number')
        try:
            user = CustomUser.objects.get(username=username, phone_number=phone_number)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError('Invalid credentials')

        data['user'] = user
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone_number']  # Add the fields you want to include