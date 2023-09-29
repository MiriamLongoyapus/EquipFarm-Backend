from django.urls import path, include
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
# from .views import PaymentListView
# from .views import PaymentDetailView
# from .views import register
# from .views import login
# from .views import FarmerDetailView
# from .views importf FarmerListView

from .import views
urlpatterns = [
  
    # path('Bookings/', BookingsListView.as_view(), name='Bookings-list-view'), 
    # path('Bookings/<int:id>/', BookingsDetailView.as_view(), name='Bookings-detail-view'),  

    # path('document/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('payments/', views.PaymentListView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', views.PaymentDetailView.as_view(), name='payment-detail'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('farmers/', views.FarmerListView.as_view(), name='user-list'),
    path('farmers/<int:id>/', views.FarmerDetailView.as_view(), name='user-list'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:id>/', views.UserDetailView.as_view(), name='user-list'),
    path('suppliers/', views.SupplierListView.as_view(), name='user-list'),
    path('suppliers/<int:id>/', views.SupplierDetailView.as_view(), name='user-list'),
    path('logout/', views.user_logout, name='user_logout'),
    path('logout_all/', views.user_logout_all, name='user_logout_all'),
    path('hirepurchases/', views.HirePurchaseListView.as_view(), name='hirepurchase-list'),
    path('hirepurchases/<int:pk>/', views.HirePurchaseDetailView.as_view(), name='hirepurchase-detail'),
    path('rentals/', views.RentalListView.as_view(), name='rental-list'),
    path('rentals/<int:pk>/', views.RentalDetailView.as_view(), name='rental-detail'),
    path('Bookings/', views.BookingListView.as_view(), name='Bookings-list'),
    path('Bookings/', views.BookingDetailView.as_view(), name='Bookings-list'),
    path('catalogue/', views.CatalogueListView.as_view(), name='catalogue-list'),
    path('catalogue/', views.CatalogueListView.as_view(), name='catalogue-list'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





