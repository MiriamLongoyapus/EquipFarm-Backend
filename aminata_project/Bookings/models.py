from django.db import models
class Bookings(models.Model):
    duration = models.DurationField()
    booking_date = models.DateField()
    customer_name = models.CharField(max_length=255, default='Customer')
    equipment_name = models.CharField(max_length=32, default='Default Equipment')
    equipment_category = models.CharField(max_length=32, default='Default Category')
    duration = models.DurationField()
    booking_date = models.DateTimeField()
  
  



    
