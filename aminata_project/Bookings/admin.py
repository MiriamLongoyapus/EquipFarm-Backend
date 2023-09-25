from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Bookings


class BookingsAdmin(admin.ModelAdmin):
    list_display = ("booking_date", "duration")
admin.site.register(Bookings, BookingsAdmin)
