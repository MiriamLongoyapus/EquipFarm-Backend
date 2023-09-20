

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from Bookings.models import Bookings
from .serializers import BookingsSerializer  
from django.shortcuts import render


class BookingsListView(APIView):
    def get(self, request):
        bookings = Bookings.objects.all()  
        serializer = BookingsSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingsDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            booking = Bookings.objects.get(id=id)
            serializer = BookingsSerializer(booking)
            return Response(serializer.data)
        except Bookings.DoesNotExist:
            return Response(f"Booking with id {id} does not exist", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, format=None):
        try:
            booking = Bookings.objects.get(id=id)
        except Bookings.DoesNotExist:
            return Response(f"Booking with id {id} does not exist", status=status.HTTP_404_NOT_FOUND)

        serializer = BookingsSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        try:
            booking = Bookings.objects.get(id=id)
        except Bookings.DoesNotExist:
            return Response(f"Booking with id {id} does not exist", status=status.HTTP_404_NOT_FOUND)

        booking.delete()
        return Response("Booking successfully deleted", status=status.HTTP_204_NO_CONTENT)


