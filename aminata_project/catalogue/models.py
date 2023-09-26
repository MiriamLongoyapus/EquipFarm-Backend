
from django.db import models
from category.models import Category

class Catalogue(models.Model):
        
       equipment_name = models.CharField(max_length=32,unique=True)
       price = models.IntegerField()
       description = models.TextField(null=True)
       image = models.ImageField(upload_to='catalogue_images/',null=True)
       is_available = models.BooleanField(default=False)  
       category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)


       def check_availability(self):
              return self.is_available
              
       def __str__(self):
                     return self.name
       class Meta:
                     verbose_name_plural = "catalog"                       

