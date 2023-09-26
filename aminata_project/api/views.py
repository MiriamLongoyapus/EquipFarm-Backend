from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from payments.models import Payment
from Hirepurchase.models import HirePurchase
from Rental.models import Rentals
from .serializers import PaymentSerializer
from .serializers import HirePurchaseSerializer
from .serializers import RentalsSerializer



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
