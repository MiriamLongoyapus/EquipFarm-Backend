from django.shortcuts import render
from rest_framework.views import APIView
from catalogue.models import Catalogue
from .serializers import CatalogueSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from category.models import Category

class CatalogueListView(APIView):
    def get(self, request):
        catalogue= Catalogue.objects.all()
        serializer = CatalogueSerializer(catalogue, many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer=CatalogueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
    
class CatalogueDetailView(APIView):
    def get(self,request, id, format=None):
        try:
            catalogue = Catalogue.objects.get(id=id)
        except Catalogue.DoesNotExist:
            return Response(
                {"error": f"Catalogue with id {id} does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = CatalogueSerializer(catalogue)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


    def put(self,request,id,format=None):
        catalogue=Catalogue.objects.get(id=id)
        serializer=CatalogueSerializer(catalogue,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format=None):
        catalogue=Catalogue.objects.get(id=id)
        catalogue.delete()
        return Response("catalogue deleted succefully",status=status.HTTP_204_NO_CONTENT)
    

class CategoryListView(APIView):
    def get(self, request):
        category= Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
    
class CategoryDetailView(APIView):
    def get(self,request, id, format=None):
        try:
            Category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            return Response(
                {"error": f"Category with id {id} does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = CategorySerializer(Category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


    def put(self,request,id,format=None):
        category=Category.objects.get(id=id)
        serializer=CategorySerializer(category,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format=None):
        category=Category.objects.get(id=id)
        category.delete()
        return Response("category deleted succefully",status=status.HTTP_204_NO_CONTENT)
    


   




   

