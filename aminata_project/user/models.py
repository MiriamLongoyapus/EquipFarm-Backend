
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models  # Add this line to import the 'models' module

ROLE_CHOICES = [
    ('farmer', 'Farmer'),
    ('supplier', 'Supplier'),
]

class CustomUser(models.Model):
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    roles = models.CharField(max_length=20,choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    pin = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name
  