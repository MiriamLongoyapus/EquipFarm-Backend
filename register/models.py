from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils.translation import gettext as _


class CustomUser(AbstractUser):
    USER_ROLES = (
        ('farmer', 'Farmer'),
        ('supplier', 'Supplier'),
        ('admin', 'Admin'),
    )
    role = models.CharField(_('Role'), max_length=15, choices=USER_ROLES, default='')
    location = models.CharField(max_length=100)
    phone_number = models.IntegerField(null=True)
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    class Meta:
        app_label = 'register'


class Farmer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    
    

class Supplier(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=100, unique=True)

 