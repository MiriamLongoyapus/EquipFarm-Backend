from django.urls import path
from .views import PaymentListView, PaymentDetailView

urlpatterns = [
    path('api/payment/', PaymentListView.as_view(), name='payment-list'),
    path('api/payment/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
]
