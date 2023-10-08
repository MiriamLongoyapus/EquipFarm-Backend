from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from register.models import CustomUser, Farmer, Supplier
from Rental.models import Rentals
from payments.models import Payment
from Hirepurchase.models import HirePurchase
from Bookings.models import Bookings
from catalogue.models import Catalogue
from category.models import Category



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
            'last_name',
            'role',
            'groups',
            'phone_number',
            'location',
            
        )
        extra_kwargs = {
            'phone_number': {'write_only': True},
        }

    def create(self, validated_data):
        confirm_phone_number = validated_data.pop('confirm_phone_number', None)

        if confirm_phone_number and validated_data['phone_number'] != confirm_phone_number:
            raise serializers.ValidationError("Phone number do not match")

        user = CustomUser.objects.create(**validated_data)
        # user.set_password(validated_data['phone_number  
        user.save()
        return user


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rentals
        fields = '__all__'
 


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
        model = Supplier
        model = Payment
        fields = '__all__'
        
class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = ("customer_name","equipment_name","booking_date","duration","equipment_category","id")


class CatalogueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogue
        fields = '__all__'        


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  