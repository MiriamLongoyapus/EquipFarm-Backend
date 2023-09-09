from django.contrib import admin

# Register your models here.
from .models import Booking
class BookingAdmin(admin.ModelAdmin):
    
    list_display=("customer_name","equipment_name","booking_date","duration",)
admin.site.register(Booking,BookingAdmin)    

