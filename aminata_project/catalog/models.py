
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=32)

class Catalog(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()  # Use TextField for longer descriptions
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # ForeignKey to Category model
    image = models.ImageField(upload_to='catalog_images/')  # Example directory for storing images

