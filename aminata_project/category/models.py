from django.db import models

class Category(models.Model):
      title=models.CharField(max_length=100)
      detail=models.TextField()
      image = models.ImageField(upload_to='catalogue_images/')
      class Meta:
          verbose_name_plural='2. Categories'
      def __str__(self):
              return self.title


