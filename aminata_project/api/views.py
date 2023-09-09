# from rest_framework import generics
# from catalog.models import  Catalog
# from .serializers import CatalogSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from catalog.models import Catalog
from .serializers import CatalogSerializer
from rest_framework.response import Response
from rest_framework import status

# class CatalogListView(generics.ListCreateAPIView):
#     queryset = Catalog.objects.all()
#     serializer_class = CatalogSerializer

# class CatalogDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Catalog.objects.all()
#     serializer_class = CatalogSerializer



class FarmerListView(APIView):
    def get(self, request):
        farmer= farmer.objects.all()  
        serializer = CatalogSerializer(farmer, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=CatalogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    