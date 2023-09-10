from django.db import models
class Catalogue(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    image = models.ImageField(upload_to='catalogue_images/')
class Meta:
        verbose_name_plural = "catalog"
