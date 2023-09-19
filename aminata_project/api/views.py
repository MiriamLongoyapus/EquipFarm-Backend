
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
from user.models import CustomUser  
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import get_user_model
from rest_framework import serializers
from user.models import Permission 
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics



User = get_user_model()

class UserListView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = RegistrationSerializer(users, many=True)  
        return Response(serializer.data)


class UserRegistrationView(generics.CreateAPIView):
    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)  
       
        
        if serializer.is_valid():
            user = serializer.save()
            
        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                username=serializer.validated_data['username'],
                phone_number=serializer.validated_data['phone_number']
            )
            if user is not None and user.roles.filter(name='Farmer').exists():
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'message': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)


        

class SupplierRegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data) 
        # phone_number = models.CharField(max_length=20)
        company_name = models.CharField(max_length=100)
        products_offered = models.TextField(max_length=100)
        # location = models.CharField(max_length=100)
        
        if serializer.is_valid():
            user = serializer.save()
            
            supplier_role, _ = Role.objects.get_or_create(name="Supplier")
            user.roles.add(supplier_role)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class FarmerLoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = authenticate(
#                 request,
#                 username=serializer.validated_data['username'],
#                 phone_number=serializer.validated_data['phone_number']
#             )
#             if user is not None and user.roles.filter(name='Farmer').exists():
#                 token, _ = Token.objects.get_or_create(user=user)
#                 return Response({'token': token.key}, status=status.HTTP_200_OK)
#         return Response({'message': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)

class SupplierLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user is not None and user.roles.filter(name='Supplier').exists():
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'message': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)

# The following views remain unchanged:
# - UserRegistrationListView
# - UserRegistrationUpdateView
# - UserRegistrationDeleteView

# from rest_framework import serializers
# from user.models import CustomUser

# class RegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'username', 'phone_number', 'location']

# class UserRegistrationView(generics.CreateAPIView):
#     def post(self, request):
#         serializer = RegistrationSerializer(data=request.data)  # Use RegistrationSerializer
#         if serializer.is_valid():
#             user = serializer.save()
            
#             farmer_role, _ = Role.objects.get_or_create(name="Farmer")
#             user.roles.add(farmer_role)
            
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SupplierRegistrationView(APIView):
#     def post(self, request):
#         serializer = RegistrationSerializer(data=request.data)  # Use RegistrationSerializer
        
#         if serializer.is_valid():
#             user = serializer.save()
            
#             supplier_role, _ = Role.objects.get_or_create(name="Supplier")
#             user.roles.add(supplier_role)
            
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
