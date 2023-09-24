from django.contrib import admin

# Register your models here.
# Register your models here.

from django.contrib import admin
from .models import Bookings


class BookingsAdmin(admin.ModelAdmin):
    list_display = ( "customer_name","equipment_name", "equipment_category", "booking_date", "duration")
admin.site.register(Bookings, BookingsAdmin)
