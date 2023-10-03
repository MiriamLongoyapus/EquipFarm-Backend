from django.contrib import admin
from .models import Bookings
class BookingsAdmin(admin.ModelAdmin):
    list_display = ("booking_date", "duration","customer_name","equipment_name","equipment_category","booking_date")
admin.site.register(Bookings, BookingsAdmin)
