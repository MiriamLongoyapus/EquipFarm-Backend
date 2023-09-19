from rest_framework import serializers
from user.models import CustomUser

# Common fields for registration
class RegistrationSerializer(serializers.ModelSerializer):
    roles= serializers.CharField(read_only=True)
    company_name=serializers.CharField(read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name','phone_number', 'company_name','roles', 'location']

    def create(self, validated_data):
    
        user = CustomUser(**validated_data)
        user.save()
        return user



# Farmer Registration Serializer
# class FarmerRegistrationSerializer(CommonRegistrationSerializer):
#     class Meta:
#         model = CustomUser
#         fields = CommonRegistrationSerializer.Meta.fields + ['username', 'phone_number', 'location']
        
#     def create(self, validated_data):
#         user = super().create(validated_data)
#         farmer_role, _ = Role.objects.get_or_create(name="Farmer")
#         user.roles.add(farmer_role)
#         return user



# # Supplier Registration Serializer
# class SupplierRegistrationSerializer(CommonRegistrationSerializer):
#     class Meta:
#         model = CustomUser
#         fields = CommonRegistrationSerializer.Meta.fields + ['phone_number', 'company_name', 'products_offered']
        
#     def create(self, validated_data):
#         user = super().create(validated_data)
#         supplier_role, _ = Role.objects.get_or_create(name="Supplier")
#         user.roles.add(supplier_role)
#         return user

# # Login Serializer
# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()  # Accept either email or username
#     password = serializers.CharField()

#     def validate(self, data):
#         username = data.get('username')
#         password = data.get('password')

#         try:
#             user = CustomUser.objects.get(models.Q(username=username) | models.Q(email=username))

#             if not user.check_password(password):
#                 raise serializers.ValidationError('Invalid credentials')
            
#             # Check if the user has the 'Farmer' or 'Supplier' role
#             if not user.roles.filter(name__in=['Farmer', 'Supplier']).exists():
#                 raise serializers.ValidationError('Invalid role for login')
#         except CustomUser.DoesNotExist:
#             raise serializers.ValidationError('Invalid credentials')
        
#         data['user'] = user
#         return data
