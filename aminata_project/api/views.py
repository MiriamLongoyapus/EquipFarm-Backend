from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from register.models import CustomUser, Farmer, Supplier
from .serializers import CustomUserSerializer, FarmerSerializer, SupplierSerializer
from rest_framework import generics



class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(role='')
    serializer_class = CustomUserSerializer

class FarmerListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(role='farmer')
    serializer_class = CustomUserSerializer

class SupplierListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(role='supplier')
    serializer_class = CustomUserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.filter(role='')
    serializer_class = CustomUserSerializer
    lookup_field='id'

class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.filter(role='supplier')
    serializer_class = CustomUserSerializer
    lookup_field='id'

class FarmerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.filter(role="farmer")
    serializer_class = CustomUserSerializer
    lookup_field='id'
   
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    role = request.data.get('role')
    if role not in ['farmer','supplier']:
        return Response({'message': 'Invalid role'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = None
    if role == 'farmer':
        serializer = CustomUserSerializer(data=request.data)
    elif role == 'supplier':
        serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data.get('phone_number'))
        user.save()

    if role == 'farmer':
            farmer = Farmer(user=user)
            farmer.save()  
        
    return Response({'message': 'Registration successful.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    username = request.data.get('username')
    phone_number = request.data.get('phone_number')
    try:
        user = CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
    if user.check_password(phone_number):
        login(request, user)
        return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def user_logout(request):
    logout(request)
    return Response({'message': 'Logged out successfully.'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def user_logout_all(request):
     logout(request)
     return Response({'message': 'Logged out of all devices  successfully.'}, status=status.HTTP_200_OK) 












