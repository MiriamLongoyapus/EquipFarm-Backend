# from django.urls import path
# from .views import UserListView,UserDetailView,FarmerRegistrationView,FarmerLoginView,SupplierRegistrationView,SupplierLoginView

# urlpatterns = [
#     path("users/", UserListView.as_view(), name="user-list"),
#     path("users/<int:id>/", UserDetailView.as_view(), name="user-detail"),
#     path("farmers/register/", FarmerRegistrationView.as_view(), name="farmer-registration"),
#     path("farmers/login/", FarmerLoginView.as_view(), name="farmer-login"),
#     path("suppliers/register/", SupplierRegistrationView.as_view(), name="supplier-registration"),
#     path("suppliers/login/", SupplierLoginView.as_view(), name="supplier-login"),
# ]  

from django.urls import path
from .views import UserRegistrationView,SupplierRegistrationView,SupplierLoginView,UserListView
from .views import UserLoginView



urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('user/register/', UserRegistrationView.as_view(), name='farmer-registration'),
    path('register/supplier/', SupplierRegistrationView.as_view(), name='supplier-registration'),
    path('login/farmer/', UserLoginView.as_view(), name='farmer-login'),
    path('login/supplier/', SupplierLoginView.as_view(), name='supplier-login'),
]
