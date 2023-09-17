from django.urls import path
from django.contrib.auth import login
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from user.models import CustomUser, Farmer, Supplier  
from .serializers import CustomUserSerializer, FarmerSerializer, SupplierSerializer  
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



class CustomUserListView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()  
        serializer = CustomUserSerializer(users, many=True)  
        return Response(serializer.data)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CustomUserDetailView(APIView):
    def get(self, request, id, format=None):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    def put(self, request, id, format=None):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id, format=None):
        user = User.objects.get(id=id)
        user.delete()
        return Response("User deleted", status=status.HTTP_204_NO_CONTENT)



class FarmerRegistrationView(APIView):
    def post(self, request):
        user = request.data.get('user')
        phone_number = request.data.get('phone_number')
        location = request.data.get('location')

        if Farmer.objects.filter(user=user).exists():
            return Response({'message': 'Username already exists'}, status=status.HTTP_409_CONFLICT)

        farmer = Farmer.objects.create(user=user, phone_number=phone_number, location=location)
        return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)


class FarmerLoginView(APIView):
    def post(self, request):
        user = request.data.get('user')
        phone_number = request.data.get('phone_number')

        try:
            farmer = Farmer.objects.get(user=user, phone_number=phone_number)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        except Farmer.DoesNotExist:
            return Response({'message': 'Invalid username or phone number'}, status=status.HTTP_401_UNAUTHORIZED)



class SupplierRegistrationView(APIView):
    def post(self, request):
        user = request.data.get('user')
        company_name = request.data.get('company_name')
        products_offered = request.data.get('products_offered')

        if Supplier.objects.filter(user=user).exists():
            return Response({'message': 'Username already exists'}, status=status.HTTP_409_CONFLICT)

        supplier = Supplier.objects.create(user=user, company_name=company_name, products_offered=products_offered)
        return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)




class SupplierLoginView(APIView):
    def post(self, request):
        user = request.data.get('user')
        company_name= request.data.get('company_name')

        try:
            supplier = Supplier.objects.get(user=user, company_name=company_name)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        except Supplier.DoesNotExist:
            return Response({'message': 'Invalid username or phone number'}, status=status.HTTP_401_UNAUTHORIZED)
            
