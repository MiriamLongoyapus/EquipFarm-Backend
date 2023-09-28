from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from payments.models import Payment
from Hirepurchase.models import HirePurchase
from Rental.models import Rentals
from .serializers import PaymentSerializer
from .serializers import HirePurchaseSerializer
from .serializers import RentalsSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from register.models import CustomUser, Farmer, Supplier
from .serializers import CustomUserSerializer, FarmerSerializer, SupplierSerializer
from rest_framework import generics

class PaymentListView(APIView):
    def get(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentDetailView(APIView):
    def get(self, request, pk):
        payment = Payment.objects.get(pk=pk)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

    def put(self, request, pk):
        payment = Payment.objects.get(pk=pk)
        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        payment = Payment.objects.get(pk=pk)
        payment.delete()
        return Response("Payment deleted", status=status.HTTP_204_NO_CONTENT)

class HirePurchaseListView(APIView):
    def get(self, request):
        hire_purchases = HirePurchase.objects.all()
        serializer = HirePurchaseSerializer(hire_purchases, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HirePurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HirePurchaseDetailView(APIView):
    def get_object(self, pk):
        try:
            return HirePurchase.objects.get(pk=pk)
        except HirePurchase.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        hire_purchase = self.get_object(pk)
        serializer = HirePurchaseSerializer(hire_purchase)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        hire_purchase = self.get_object(pk)
        serializer = HirePurchaseSerializer(hire_purchase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        hire_purchase = self.get_object(pk)
        hire_purchase.delete()
        return Response("HirePurchase deleted", status=status.HTTP_204_NO_CONTENT)



class RentalListView(APIView):
    def get(self, request):
        rentals = Rentals.objects.all()  # Use Rentals model
        serializer = RentalsSerializer(rentals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RentalDetailView(APIView):
    def get(self, request, pk):
        rentals = Rentals.objects.get(pk=pk)
        serializer = RentalsSerializer(rental)
        return Response(serializer.data)

    def put(self, request, pk):
        rental = Rental.objects.get(pk=pk)
        serializer = RentalsSerializer(rental, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        rental = Rentals.objects.get(pk=pk)
        rental.delete()
        return Response("Rental deleted", status=status.HTTP_204_NO_CONTENT)


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
    required_field='id'

class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.filter(role='supplier')
    serializer_class = CustomUserSerializer
    required_field='id'

class FarmerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.filter(role="farmer")
    serializer_class = CustomUserSerializer
    required_field='id'

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    role = request.data.get('role')
    if role not in ['farmer', 'supplier']:
        return Response({'message': 'Invalid role'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data.get('phone_number'))
        user.save()

        if role == 'supplier':
            company_name = request.data.get('company_name')
            if not company_name:
                user.delete() 
                return Response({'error': 'Company name cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)

            supplier = Supplier(user=user, company_name=company_name)
            supplier.save()
        elif role == 'farmer':
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
