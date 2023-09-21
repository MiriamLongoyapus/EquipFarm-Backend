from django.urls import path
from .views import FarmerRegistrationView, FarmerLoginView, SupplierRegistrationView, SupplierLoginView, LoginView, UserListView

urlpatterns = [
    path('register/farmer/', FarmerRegistrationView.as_view(), name='farmer-registration'),
    path('login/farmer/', FarmerLoginView.as_view(), name='farmer-login'),
    path('register/supplier/', SupplierRegistrationView.as_view(), name='supplier-registration'),
    path('login/supplier/', SupplierLoginView.as_view(), name='supplier-login'), 
    path('login/<str:user_type>/', LoginView.as_view(), name='user-login'),
    path('users/', UserListView.as_view(), name='user-list'),  

]
