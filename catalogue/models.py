from django.db import models
from category.models import Category   

class Catalogue(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    equipment_name = models.CharField(max_length=32, unique=True)
    price = models.IntegerField()
    description = models.TextField(null=True)
    
    in_stock=models.PositiveBigIntegerField(default=1)
    image = models.URLField(max_length=2000,null=True)
    is_available = models.BooleanField(default=False)

    def check_availability(self):
        return self.is_available

    def increment_stock(self, quantity):
        if quantity > 0:
            self.in_stock += quantity
            self.save()

    def decrement_stock(self, quantity):
        if quantity > 0 and self.in_stock >= quantity:
            self.in_stock -= quantity
            self.save()

    def __str__(self):
        return self.equipment_name


    class Meta:
       app_label = 'category'
