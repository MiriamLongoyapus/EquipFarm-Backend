
from django.urls import path
from .import views



from django.urls import path
from .views import BookingsListView, BookingsDetailView

urlpatterns = [ 
    path('Bookings/', BookingsListView.as_view(), name='Bookings_list_view'), 
    path('Bookings/<int:id>/', BookingsDetailView.as_view(), name='Bookings_detail_view'), 
    

]





from django.urls import path,include
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from .views import CatalogueListView
from .views import CatalogueDetailView



schema_view = get_schema_view(
    openapi.Info(
        title="Catalogue",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    
    path('payments/', views.PaymentListView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', views.PaymentDetailView.as_view(), name='payment-detail'),

    
    path('hirepurchases/', views.HirePurchaseListView.as_view(), name='hirepurchase-list'),
    path('hirepurchases/<int:pk>/', views.HirePurchaseDetailView.as_view(), name='hirepurchase-detail'),


    path('rentals/', views.RentalListView.as_view(), name='rental-list'),
    path('rentals/<int:pk>/', views.RentalDetailView.as_view(), name='rental-detail'),
]
