
from django.db import models
# import uuid
# import random

class Bookings(models.Model):
#     customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    equipment_name = models.CharField(max_length=32)
    equipment_category = models.CharField(max_length=32)
    duration = models.DurationField()
    booking_date = models.DateTimeField()
  
   
