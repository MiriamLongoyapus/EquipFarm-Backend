from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=100)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_users', 
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_users',  
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

class Supplier(models.Model):
    user = models.CharField(max_length=255)
    company_name = models.CharField(max_length=100)
    products_offered = models.TextField()

class Farmer(models.Model):
    user = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=255, default="Unknown")

    # farm_size = models.IntegerField() 
    # crops_grown = models.TextField()
