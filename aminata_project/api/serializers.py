from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from register.models import CustomUser, Farmer, Supplier

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'role',
            'groups',
            'phone_number',
            
        )
        extra_kwargs = {
            'phone_number': {'write_only': True},
        }

    def create(self, validated_data):
        confirm_phone_number = validated_data.pop('confirm_phone_number', None)

        if confirm_phone_number and validated_data['phone_number'] != confirm_phone_number:
            raise serializers.ValidationError("Phone number do not match")

        user = CustomUser.objects.create(**validated_data)
        # user.set_password(validated_data['phone_number'])  
        user.save()
        return user



from rest_framework import serializers
from Bookings.models import Bookings

class BookingsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Bookings
       fields = "__all__" 


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

from rest_framework import serializers
from catalogue.models import  Catalogue

class CatalogueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogue
        fields = '__all__'
