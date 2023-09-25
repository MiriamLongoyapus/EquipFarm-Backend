from django.urls import path
from . import views
from .views import CartListView
from .views import CartDetailView

urlpatterns = [
    path('carts/', CartListView.as_view(), name='cart-list'),
    path('carts/<int:id>/', CartDetailView.as_view(), name='cart-detail'),
]   