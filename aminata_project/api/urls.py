

from django.urls import path
from .views import BookingsListView, BookingsDetailView

urlpatterns = [ 
    path('Bookings/', BookingsListView.as_view(), name='Bookings_list_view'), 
    path('Bookings/<int:id>/', BookingsDetailView.as_view(), name='Bookings_detail_view'), 
    

]





from django.urls import path,include
from django.conf.urls.static import static
from rest_framework import permissions
from django.conf import settings
from .views import CatalogueListView, CategoryDetailView, CategoryListView
from .views import CatalogueDetailView


urlpatterns = [
    path('catalogue/', CatalogueListView.as_view(), name='catalogue-list-create'),
    path('catalogue/<int:id>/', CatalogueDetailView.as_view(), name='catalogue-detail'),
    path('category/', CategoryListView.as_view(), name='catalogue-list-create'),
    path('category/<int:id>/', CategoryDetailView.as_view(), name='catalogue-detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



