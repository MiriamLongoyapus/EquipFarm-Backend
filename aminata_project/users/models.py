from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=100)
    permissions = models.ManyToManyField(Permission, related_name='roles')

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users', blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True)
    products_offered = models.TextField(blank=True)
    roles = models.ManyToManyField(Role, related_name='users', blank=True)
    # role = models.CharField(_('Role'), max_length=15, choices=USER_ROLES, default='regular_user')







    def is_farmer(self):
        return hasattr(self, 'farmer')

    def is_supplier(self):
        return hasattr(self, 'supplier')

    is_farmer.boolean = True
    is_supplier.boolean = True
