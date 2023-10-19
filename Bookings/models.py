from django.db import models
from register.models import CustomUser

class Bookings(models.Model):
    

    image = models.URLField(max_length=2000,null=True)
    duration = models.DurationField()
    customer_name = models.CharField(max_length=255, default='Customer')
    equipment_name = models.CharField(max_length=32, default='Default Equipment')
    equipment_category = models.CharField(max_length=32, default='Default Category')
    booking_date = models.DateTimeField()
    phone_number = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    # amount = models.DecimalField(max_digits=10, decimal_places=2)  
    date_returned = models.DateTimeField(null=True, blank=True)  
  


   













    
