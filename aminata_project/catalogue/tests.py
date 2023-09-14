from django.test import TestCase
from .models import Catalogue

class CatalogueModelTestCase(TestCase):
    def setUp(self):
        self.catalogue = Catalogue.objects.create(
            name="Test Catalogue",
            description="This is a test catalogue",
            image="catalogue_images/test.jpg"  
        )

    def test_catalogue_creation(self):
        self.assertEqual(self.catalogue.name, "Test Catalogue")
        self.assertEqual(self.catalogue.description, "This is a test catalogue")
        self.assertEqual(self.catalogue.image, "catalogue_images/test.jpg")

    def test_verbose_name_plural(self):
        self.assertEqual(str(Catalogue._meta.verbose_name_plural), "catalog")



        from django.test import TestCase
from .models import Catalogue

class CatalogueModelTestCase(TestCase):
    def setUp(self):
        self.catalogue = Catalogue.objects.create(
            name="Test Catalogue",
            description="This is a test catalogue",
            image="catalogue_images/test.jpg"  
        )

    def test_catalogue_creation(self):
        self.assertEqual(self.catalogue.name, "Test Catalogue")
        self.assertEqual(self.catalogue.description, "This is a test catalogue")
        self.assertEqual(self.catalogue.image, "catalogue_images/test.jpg")

    def test_verbose_name_plural(self):
        self.assertEqual(str(Catalogue._meta.verbose_name_plural), "catalog")

    def test_catalogue_str_method(self):
        """
        Test the __str__ method of the Catalogue model.
        """
        expected_str = "Test Catalogue"  
        self.assertEqual(str(self.catalogue), expected_str)

    def test_catalogue_update(self):
        """
        Test updating attributes of a Catalogue instance.
        """
        new_name = "Updated Catalogue Name"
        new_description = "This catalogue has been updated"
        new_image = "catalogue_images/updated.jpg"

        self.catalogue.name = new_name
        self.catalogue.description = new_description
        self.catalogue.image = new_image
        self.catalogue.save()

        updated_catalogue = Catalogue.objects.get(pk=self.catalogue.pk)

        self.assertEqual(updated_catalogue.name, new_name)
        self.assertEqual(updated_catalogue.description, new_description)
        self.assertEqual(updated_catalogue.image, new_image)

    def test_catalogue_deletion(self):
        """
        Test deleting a Catalogue instance.
        """
        catalogue_count_before_deletion = Catalogue.objects.count()
        self.catalogue.delete()
        catalogue_count_after_deletion = Catalogue.objects.count()

        self.assertEqual(catalogue_count_before_deletion - 1, catalogue_count_after_deletion)

    def test_catalogue_manager(self):
        """
        Test using a custom manager method if you have one.
        """
        pass

    def test_catalogue_validation(self):
        """
        Test model validation for the Catalogue instance.
        """
        pass

    def test_catalogue_query(self):
        """
        Test querying the Catalogue model.
        """
        pass

