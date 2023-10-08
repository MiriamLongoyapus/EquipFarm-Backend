from django.db import models
from catalogue.models import Catalogue

class Rentals(models.Model):
    equipment_name = models.ForeignKey(Catalogue,on_delete=models.CASCADE)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    rental_period = models.DurationField()
    date = models.DateField(auto_now_add=True)
    duration_period = models.CharField(   
        max_length=20,
        choices=[('week', 'Week'), ('day', ' Day')],null=True) 
    total_rental_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calculate_total_cost(self):
        if self.duration_period == 'week':
            self.total_rental_cost = float(self.rental_price) * (self.rental_period.days / 7)
        elif self.duration_period == 'day':
            self.total_rental_cost = float(self.rental_price) * self.rental_period.days
        else:
            self.total_rental_cost = float(0)
    def save(self, *args, **kwargs):
        self.calculate_total_cost()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Rental for {self.equipment_name}'


