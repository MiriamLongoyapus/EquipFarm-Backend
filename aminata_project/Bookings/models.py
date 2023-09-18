from django.db import models
# from users.models import CustomUser 


class Bookings(models.Model):
#     customer_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     equipment_name = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=32)
    equipment_name = models.CharField(max_length=32)
    equipment_category = models.CharField(max_length=32)
    duration = models.DurationField()
    booking_date = models.DateTimeField()
  
  



   
