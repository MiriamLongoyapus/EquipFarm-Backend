from django.contrib import admin
from .models import Catalogue

class CatalogueAdmin(admin.ModelAdmin):
    list_display=('image',)
    
    
admin.site.register(Catalogue,CatalogueAdmin)






