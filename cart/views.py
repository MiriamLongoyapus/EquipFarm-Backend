from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView
  
from .models import Cart  
from catalogue.models import Catalogue
from rest_framework import status, generics
from .serializers import CartSerializer


class CartListView(APIView):
    # queryset = Cart.objects.all()
    # serializer_class = CartSerializer
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

class AddToCartView(APIView):
    # serializer_class = CartSerializer

    def post(self, request, pk):
        try:
            catalogue = Catalogue.objects.get(pk=pk)
            cart_item = Cart(user=request.user, catalogue=catalogue)
            cart_item.save()
            serializer = CartSerializer(cart_item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Catalogue.DoesNotExist:
            return Response({"error": 'Catalogue item not found'}, status=status.HTTP_404_NOT_FOUND)

class RemoveFromCartView(APIView):
    def delete(self, request, pk):
        try:
            cart_item = Cart.objects.get(user=request.user, catalogue_id=pk)
            cart_item.delete()
            return Response({"message": "Item removed from cart"}, status=status.HTTP_204_NO_CONTENT)
        except Cart.DoesNotExist:
            return Response({"error": "Item not found in the Cart"}, status=status.HTTP_404_NOT_FOUND)


class ViewCartView(APIView):
    def get(self, request):
        cart_items = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(cart_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)        

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