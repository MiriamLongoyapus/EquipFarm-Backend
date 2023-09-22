
from django.db import models

class Category(models.Model):
      title=models.CharField(max_length=100)
      detail=models.TextField()
      image = models.ImageField(upload_to='catalogue_images/')
      class Meta:
          verbose_name_plural='2. Categories'
      def __str__(self):
              return self.title



class Catalogue(models.Model):
        
        name = models.CharField(max_length=32,unique=True)
        price = models.IntegerField()
        description = models.TextField(null=True)
        image = models.ImageField(upload_to='catalogue_images/',null=True)
        is_available = models.BooleanField(default=False)  # Add this field
        category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)


        def check_availability(self):
         return self.is_available
        
        def __str__(self):
               return self.name
        class Meta:
              verbose_name_plural = "catalog"                       






              

