# from django.shortcuts import renrenderder
#  from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from payment.models import Payment
from .serializers import PaymentSerializer

class PaymentListView(APIView):
    def get(self, request):
        payment = Payment.objects.all()
        serializer = PaymentSerializer(payment, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class PaymentDetailView(APIView):
    def get(self,request,id,format=None):
        payment = Payment.objects.get(id=id)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)
    def put(self,request,id,format=None):
        payment= Payment.objects.get(id=id)
        serializer = PaymentSerializer(payment,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # def put(self,request,id,format=None):
    #     payment= Payment.objects.get(id=id)
    #     payment.delete()
    #     return Response("payment deleted", status=status.HTTP_204_NO_CONTENT)
    def delete(self,request,id,format=None):
        payment=Payment.objects.get(id=id)
        payment.delete()
        return Response("payment with id {id} succefully deleted",status=status.HTTP_204_NO_CONTENT)