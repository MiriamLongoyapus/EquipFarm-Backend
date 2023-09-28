from django.db import models
# from users.models import CustomUser 

class Bookings(models.Model):
    #customer_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    #equipment_name = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    # equipment_category = models.ForeignKey(Category,on_delete=models)
    duration = models.DurationField()
    booking_date = models.DateField()
    

    



    
