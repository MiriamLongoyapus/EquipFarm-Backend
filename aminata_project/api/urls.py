from django.urls import path
from .views import CustomUserListView,CustomUserDetailView,FarmerRegistrationView,FarmerLoginView,SupplierRegistrationView,SupplierLoginView

urlpatterns = [
    path("users/", CustomUserListView.as_view(), name="user-list"),
    path("users/<int:id>/", CustomUserDetailView.as_view(), name="user-detail"),
    path("farmers/register/", FarmerRegistrationView.as_view(), name="farmer-registration"),
    path("farmers/login/", FarmerLoginView.as_view(), name="farmer-login"),
    path("suppliers/register/", SupplierRegistrationView.as_view(), name="supplier-registration"),
    path("suppliers/login/", SupplierLoginView.as_view(), name="supplier-login"),
]