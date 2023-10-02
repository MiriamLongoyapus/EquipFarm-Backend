
from django.test import TestCase
from .models import Category, Catalogue

class CategoryModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            title="Test Category",
            detail="Test category detail",
        )

    def test_category_creation(self):
        self.assertEqual(self.category.title, "Test Category")
        self.assertEqual(self.category.detail, "Test category detail")

class CatalogueModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            title="Test Category",
            detail="Test category detail",
        )
        self.catalogue = Catalogue.objects.create(
            name="Test Product",
            price=100,  
            description="Test product description",
            category=self.category,
        )

    def test_catalogue_creation(self):
        self.assertEqual(self.catalogue.name, "Test Product")
        self.assertEqual(self.catalogue.price, 100)  
        self.assertEqual(self.catalogue.description, "Test product description")
        self.assertEqual(self.catalogue.category, self.category)

    def test_catalogue_str_method(self):
        self.assertEqual(str(self.catalogue), "Test Product")
