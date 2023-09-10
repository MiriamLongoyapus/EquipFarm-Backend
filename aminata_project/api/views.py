from django.shortcuts import render
from rest_framework.views import APIView
from catalogue.models import Catalogue
from .serializers import CatalogueSerializer
from rest_framework.response import Response
from rest_framework import status

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
        Catalogue=Catalogue.objects.get(id=id)
        serializer=CatalogueSerializer(Catalogue,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format=None):
        Catalogue=Catalogue.objects.get(id=id)
        Catalogue.delete()
        return Response("catalogue successfully deleted",status=status.HTTP_204_NO_CONTENT)
   

 