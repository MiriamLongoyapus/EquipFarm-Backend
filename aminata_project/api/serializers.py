


from rest_framework import serializers
from Bookings.models import Bookings

class BookingsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Bookings
       fields = "__all__" 





from rest_framework import serializers
from catalogue.models import  Catalogue

class CatalogueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogue
        fields = '__all__'
