from django.urls import path
from . import views
from .views import CartListView
from .views import CartDetailView, AddToCartView, RemoveFromCartView, ViewCartView
urlpatterns = [
    path('carts/', CartListView.as_view(), name='cart-list'),
    path('carts/<int:id>/', CartDetailView.as_view(), name='cart-detail'),
    path('carts/view-cart/', ViewCartView.as_view(), name="view-cart"),
    path('carts/add-to-cart/<int:pk>/', AddToCartView.as_view(), name="add-to-cart"),
    path('carts/remove-from-cart/<int:pk>/', RemoveFromCartView.as_view(), name="remove-from-cart"),
   
]   