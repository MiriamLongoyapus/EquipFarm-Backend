from django.test import TestCase
from .models import Category

class CategoryModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(
            title="Test Category",
            detail="This is a test category",
            image="catalogue_images/test_image.jpg"
        )

    def test_category_creation(self):
        self.assertEqual(self.category.title, "Test Category")
        self.assertEqual(self.category.detail, "This is a test category")

    def test_category_str_method(self):
        self.assertEqual(str(self.category), "Test Category")
