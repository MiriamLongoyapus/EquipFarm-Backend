from django.urls import path
from .views import PaymentListView,PaymentDetailView

urlpatterns = [
path('payment/', PaymentListView.as_view(), name='payment_list_view'),
path('payment/<int:id>/', PaymentDetailView.as_view(), name='payment_detail_view'),
]