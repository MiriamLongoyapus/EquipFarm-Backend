
from django.db import models

class Catalog(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()  
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    image = models.ImageField(upload_to='catalog_images/')  
