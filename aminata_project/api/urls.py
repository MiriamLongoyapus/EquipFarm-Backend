from django.urls import path
from .import views

from . import views
urlpatterns = [
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
]
