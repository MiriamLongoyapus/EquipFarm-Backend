from django.db import models


class Category(models.Model):
    DAIRY_CHOICES = [
        ("milking_machine", "Milking-machine"),
        ("milk_pasteurizer", "Milk_pasteurizer"),
        ("cow_brushes", "Cow_brushes"),
        ("testing_equipment", "Testing_equipment"),
    ]
    FARM_CHOICES = [
        ("plow", "Plow"),
        ("harrow", "Harrow"),
        ("planter", "Planter"),
    ]
    POUTRY_CHOICES = [
        ("nesting_boxes", "Nesting_boxes"),
        ("egg_incubators", "Egg_incubators"),
        ("automatic_waterers", "Automatic_waterers"),
    ]
  
    farm = models.CharField(choices=FARM_CHOICES, max_length=20, default='plow')
    poultry = models.CharField(choices=POUTRY_CHOICES, max_length=20,default='nesting_boxes')
    dairy =  models.CharField(choices=DAIRY_CHOICES, max_length=20, default='milking_machine')


    def __str__(self):  
     return self.get_dairy_display() if self.dairy else (self.get_farm_display() if self.farm else self.get_poultry_display())
 