from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView
  
from .models import Cart  
from rest_framework import status
from .serializers import CartSerializer
class CartListView(APIView):
    def get(self, request):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            cart = Cart.objects.get(id=id)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        try:
            cart = Cart.objects.get(id=id)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        try:
            cart = Cart.objects.get(id=id)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        cart.delete()
        return Response("Cart deleted", status=status.HTTP_204_NO_CONTENT)