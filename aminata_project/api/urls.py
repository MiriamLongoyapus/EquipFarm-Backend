# from django.urls import path
# from .views import PaymentListView, PaymentDetailView

# urlpatterns = [
#     path('payment/', PaymentListView.as_view(), name='payment_list_view'),
#     # path('payment/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail')
#     path('payment/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
#     from django.urls import path
from .views import PaymentListView, PaymentDetailView
from django.urls import path

urlpatterns = [
    path('payment/', PaymentListView.as_view(), name='payment_list_view'),
    path('payment/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
]
