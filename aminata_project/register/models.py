from django.db import models

# Create your models here.

# Create your models here.
# from django.contrib.auth.models import AbstractUser, Group, Permission
# from django.db import models
# from django.utils.translation import gettext_lazy as _
# from phonenumber_field.modelfields import PhoneNumberField


# class User(AbstractUser):
#     phone_number =PhoneNumberField(max_length=100)
#     # location = models.CharField(max_length=100)


#     is_farmer = models.BooleanField(default=False)
#     is_supplier = models.BooleanField(default=False)

#     groups = models.ManyToManyField(
#         Group,
#         verbose_name=_('groups'),
#         blank=True,
#         related_name='custom_user_set',  
#     )

#     user_permissions = models.ManyToManyField(
#         Permission,
#         verbose_name=_('user permissions'),
#         blank=True,
#         related_name='custom_user_set_permissions',  
#     )

# class Farmer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     # first_name = models.CharField(max_length=100)
#     # last_name = models.CharField(max_length=100)
#     # phone_number = models.CharField(max_length=100)
    # location = models.CharField(max_length=100)
   
# class Supplier(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     # first_name = models.CharField(max_length=100)
#     # last_name = models.CharField(max_length=100)
#     # phone_number = models.CharField(max_length=100)
    # company_name = models.CharField(max_length=100, unique=True)
from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    USER_ROLES = (
        ('farmer', 'Farmer'),
        ('supplier', 'Supplier'),
        ('admin', 'Admin'),
    )
    role = models.CharField(_('Role'), max_length=15, choices=USER_ROLES, default='')
    location = models.CharField(max_length=100)
    phone_number = PhoneNumberField(_('Phone Number'), blank=True, null=True)
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

    # def __str__(self):
    #     return self.phone_number


class Farmer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
   


class Supplier(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=110, unique=True)

   
    
