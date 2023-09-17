from django.test import TestCase
from .models import User
class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            first_name="Equip",
            last_name="Farm",
            email="equipfarm@gmail.com",
            phone_number="0790448832",
            location="Turkey",
        )
    def test_first_name_label(self):
        user = User.objects.get(id=self.user.id)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_last_name_label(self):
        user = User.objects.get(id=self.user.id)
        field_label = user._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_email_label(self):
        user = User.objects.get(id=self.user.id)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_phone_number_label(self):
        user = User.objects.get(id=self.user.id)
        field_label = user._meta.get_field('phone_number').verbose_name
        self.assertEqual(field_label, 'phone number')

    def test_location_label(self):
        user = User.objects.get(id=self.user.id)
        field_label = user._meta.get_field('location').verbose_name
        self.assertEqual(field_label, 'location')

    # def test_email_unique(self):
    #     with self.assertRaises(Exception) as context:
    #         User.objects.create(
    #             first_name="Miriam",
    #         last_name="Farm",
    #         email="equipfarm@gmail.com",
    #         phone_number="0790448832",
    #         location="Nakuru",
    #         )
    #     self.assertTrue('unique constraint' in str(context.exception))
    # def test_str_method(self):
    #     user = User.objects.get(id=self.user.id)
    #     self.assertEqual(str(user), 'Equip')