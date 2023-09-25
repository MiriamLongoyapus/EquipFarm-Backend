from django.db import models
# from users.models import CustomUser 

class Bookings(models.Model):
    #customer_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    #equipment_name = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    # equipment_category = models.ForeignKey(EquipmentCategory,on_delete=models.CASCADE)
    duration = models.DurationField()
    booking_date = models.DateField()
    

    



    