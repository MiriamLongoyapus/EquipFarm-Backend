


from rest_framework import serializers
from Bookings.models import Bookings

class BookingsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Bookings
       fields = "__all__" 





from rest_framework import serializers
from catalogue.models import  Catalogue
from category.models import  Category


class CatalogueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogue
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

