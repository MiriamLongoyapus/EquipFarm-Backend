from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from payment.models import Payment
from .serializers import PaymentSerializer


class PaymentListView(APIView):
    def get(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)
      

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class PaymentDetailView(APIView):
    def get(self, request, pk, format=None):
        payment = get_object_or_404(Payment, pk=pk)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

    def put(self,request,id,format=None):
        catalogue=Catalogue.objects.get(id=id)
        serializer=CatalogueSerializer(catalogue,request.data)
    def put(self, request, pk, format=None):
        payment = get_object_or_404(Payment, pk=pk)
        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
        catalogue=Catalogue.objects.get(id=id)
        catalogue.delete()
        return Response("catalogue deleted succefully",status=status.HTTP_204_NO_CONTENT)


        return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        payment = get_object_or_404(Payment, pk=pk)
        payment.delete()
        return Response("Payment deleted", status=status.HTTP_204_NO_CONTENT)

class PaymentListView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer