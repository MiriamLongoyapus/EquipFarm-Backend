from django.urls import path
from .import views

urlpatterns = [
    
    path('payments/', views.PaymentListView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', views.PaymentDetailView.as_view(), name='payment-detail'),

    
    path('hirepurchases/', views.HirePurchaseListView.as_view(), name='hirepurchase-list'),
    path('hirepurchases/<int:pk>/', views.HirePurchaseDetailView.as_view(), name='hirepurchase-detail'),


    path('rentals/', views.RentalListView.as_view(), name='rental-list'),
    path('rentals/<int:pk>/', views.RentalDetailView.as_view(), name='rental-detail'),
]
