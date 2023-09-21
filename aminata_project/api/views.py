from .serializers import CommonRegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
from users.models import CustomUser
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import permission_required
from users.models import Role
from django.contrib.auth import get_user_model
from .serializers import FarmerRegistrationSerializer, SupplierRegistrationSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import Role
from .serializers import FarmerRegistrationSerializer
from django.contrib.auth import get_user_model
from django.db.models import Q  



User = get_user_model()

class FarmerRegistrationView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')  
        
        try:
            user = CustomUser.objects.get(username=username)
            return Response({'error': 'User with this username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            pass 
        
        serializer = FarmerRegistrationSerializer(data=data)
        
        if serializer.is_valid():
            farmer = serializer.save()
            farmer_role, _ = Role.objects.get_or_create(name="Farmer")
            farmer.roles.add(farmer_role)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FarmerLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            phone_number = serializer.validated_data.get('phone_number')
            
            try:
                user = CustomUser.objects.get(username=username)
                if user.phone_number == phone_number:
                 
                    return Response({'message': 'Successfully logged in'}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            except CustomUser.DoesNotExist:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)




class SupplierRegistrationView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username') 
        
        try:
            user = CustomUser.objects.get(username=username)
            return Response({'error': 'User with this username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            pass  
        
        serializer = SupplierRegistrationSerializer(data=data)
        
        if serializer.is_valid():
            supplier = serializer.save()
            supplier_role, _ = Role.objects.get_or_create(name="Supplier")
            supplier.roles.add(supplier_role)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SupplierLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            phone_number = serializer.validated_data.get('phone_number')
            
            try:
                user = CustomUser.objects.get(username=username)
                if user.phone_number == phone_number:
                  
                    return Response({'message': 'Successfully logged in'}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            except CustomUser.DoesNotExist:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LoginView(APIView):
    def post(self, request, user_type):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            phone_number = serializer.validated_data.get('phone_number')
            try:
                if user_type == 'farmer':
                    user = CustomUser.objects.get(Q(username=username), roles__name='Farmer')
                elif user_type == 'supplier':
                    user = CustomUser.objects.get(Q(username=username), roles__name='Supplier')
                else:
                    return Response({'message': 'Invalid user type'}, status=status.HTTP_400_BAD_REQUEST)
                if not user.check_phone_number(phone_number):
                    return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            except CustomUser.DoesNotExist:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


from .serializers import UserSerializer  # Import the UserSerializer
from users.models import CustomUser
class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer  # Replace 'UserSerializer' with your serializer for the User model
    permission_classes = [IsAuthenticated]  # Add any permissions you need