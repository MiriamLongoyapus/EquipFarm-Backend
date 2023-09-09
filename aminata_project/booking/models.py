from django.db import models

# Create your models here.

# # Create your models here.
class Booking (models.Model):
    customer_name = models.CharField(max_length=32)
    equipment_name=models.CharField(max_length=32)
    duration=models.DurationField()
    booking_date =models.DateTimeField()
    

   
def __str__(self):
        return self.customer_name