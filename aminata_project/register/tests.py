from django.test import TestCase
from django.contrib.auth.models import Group, Permission, ContentType
from phonenumber_field.phonenumber import PhoneNumber
from .models import CustomUser, Farmer, Supplier

class CustomUserTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            role='farmer',
            location='Test Location',
            phone_number='+1234567890'
        )
        self.group = Group.objects.create(name='Test Group')

        content_type = ContentType.objects.get_for_model(CustomUser)

        self.permission = Permission.objects.create(
            name='Test Permission Unique',
            codename='test_permission_unique',
            content_type=content_type
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.role, 'farmer')
        self.assertEqual(self.user.location, 'Test Location')
        self.assertEqual(self.user.phone_number, PhoneNumber.from_string('+1234567890'))

    def test_user_groups(self):
        self.user.groups.add(self.group)
        self.assertIn(self.group, self.user.groups.all())

    def test_user_permissions(self):
        self.user.user_permissions.add(self.permission)
        self.assertIn(self.permission, self.user.user_permissions.all())

