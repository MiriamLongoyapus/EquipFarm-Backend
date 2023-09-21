from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=100)
    permissions = models.ManyToManyField(Permission, related_name='roles')

class CustomUser(AbstractUser):
    roles = models.ManyToManyField(Role, related_name='users')
    groups = models.ManyToManyField(Group, related_name='custom_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users', blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)  
    company_name = models.CharField(max_length=255, blank=True)
    products_offered = models.TextField(blank=True)

    is_farmer = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.roles.filter(name='Farmer').exists():
            self.is_farmer = True
        if self.roles.filter(name='Supplier').exists():
            self.is_supplier = True
        super().save(*args, **kwargs)

    def is_farmer(self):
        return self.is_farmer

    def is_supplier(self):
        return self.is_supplier
    


