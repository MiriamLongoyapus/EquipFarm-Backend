
from django.db import models

class Catalogue(models.Model):
        
        name = models.CharField(max_length=32,unique=True)
        description = models.TextField()
        image = models.ImageField(upload_to='catalogue_images/')
        
        def __str__(self):
               return self.name
        class Meta:
              verbose_name_plural = "catalog"                       






              

