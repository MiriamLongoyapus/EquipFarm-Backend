


from rest_framework import serializers
from Bookings.models import Bookings

class BookingsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Bookings
       fields = "__all__" 





