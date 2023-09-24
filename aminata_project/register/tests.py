from django.test import TestCase
from django.contrib.auth.models import Group
from .models import CustomUser, Farmer, Supplier
from phonenumber_field.phonenumber import PhoneNumber

class CustomUserModelTestCase(TestCase):
    def setUp(self):
        self.group = Group.objects.create(name='Test Group')

    def test_create_custom_user(self):
        user = CustomUser.objects.create(
            username='testuser',
            role='farmer',
            location='Test Location',
            phone_number=PhoneNumber.from_string('+1234567890'),
        )
        user.groups.add(self.group)

        self.assertEqual(user.role, 'farmer')
        self.assertEqual(user.location, 'Test Location')
        self.assertEqual(user.phone_number, PhoneNumber.from_string('+1234567890'))
        self.assertTrue(user.groups.filter(name='Test Group').exists())

class FarmerModelTestCase(TestCase):
    def test_create_farmer(self):
        user = CustomUser.objects.create(
            username='testfarmer',
            role='farmer',
            location='Test Location',
            phone_number=PhoneNumber.from_string('+1234567890'),
        )
        farmer = Farmer.objects.create(user=user)

        self.assertEqual(farmer.user, user)

class SupplierModelTestCase(TestCase):
    def test_create_supplier(self):
        user = CustomUser.objects.create(
            username='testsupplier',
            role='supplier',
            location='Test Location',
            phone_number=PhoneNumber.from_string('+1234567890'),
        )
        supplier = Supplier.objects.create(user=user, company_name='Test Company')

        self.assertEqual(supplier.user, user)
        self.assertEqual(supplier.company_name, 'Test Company')

class GroupPermissionTestCase(TestCase):
    def test_create_group_with_permissions(self):
        permission = Permission.objects.create(
            codename='can_view_custom_user',
            name='Can view custom user',
            content_type_id=CustomUser._meta.content_type_id,
        )

        group = Group.objects.create(name='Test Group')
        group.permissions.add(permission)

        user = CustomUser.objects.create(
            username='testuser',
            role='farmer',
            location='Test Location',
            phone_number=PhoneNumber.from_string('+254740075989'),
        )
        user.groups.add(group)

        self.assertTrue(user.has_perm('auth.view_customuser'))
