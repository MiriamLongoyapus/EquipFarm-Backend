from django.db import models
# from users.models import CustomUser 

class Bookings(models.Model):
    duration = models.DurationField()
    booking_date = models.DateField()
    customer_name = models.CharField(max_length=32)
    equipment_name = models.CharField(max_length=32)
    equipment_category = models.CharField(max_length=32)
    duration = models.DurationField()
    booking_date = models.DateTimeField()
  
  



    
