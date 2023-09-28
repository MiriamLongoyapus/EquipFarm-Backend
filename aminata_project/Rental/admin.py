from django.contrib import admin
from .models import Rentals

class RentalsAdmin(admin.ModelAdmin):
    class Meta:
        model = Rentals
        fields = '__all__'

admin.site.register(Rentals, RentalsAdmin)
