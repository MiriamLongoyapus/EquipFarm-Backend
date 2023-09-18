from django.test import TestCase
from .models import CustomUser, Supplier, Farmer

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            username='testuser',
            phone_number='1234567890',
            location='Test Location',
        )

    def test_custom_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.phone_number, '1234567890')
        self.assertEqual(self.user.location, 'Test Location')

    def test_custom_user_str_representation(self):
        self.assertEqual(str(self.user), 'testuser')

class SupplierModelTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            username='supplieruser',
            phone_number='1234567890',
            location='Supplier Location',
        )

        self.supplier = Supplier.objects.create(
            user=self.user,
            company_name='Supplier Company',
            products_offered='Product 1, Product 2',
        )

    def test_supplier_creation(self):
        self.assertEqual(self.supplier.user.username, 'supplieruser')
        self.assertEqual(self.supplier.company_name, 'Supplier Company')
        self.assertEqual(self.supplier.products_offered, 'Product 1, Product 2')

    def test_supplier_user_association(self):
        self.assertEqual(self.supplier.user, self.user)

class FarmerModelTestCase(TestCase):
    def setUp(self):
        self.farmer = Farmer.objects.create(
            user='farmeruser',
            phone_number='9876543210',
            location='Farmer Location',
        )

    def test_farmer_creation(self):
        self.assertEqual(self.farmer.user, 'farmeruser')
        self.assertEqual(self.farmer.phone_number, '9876543210')
        self.assertEqual(self.farmer.location, 'Farmer Location')


