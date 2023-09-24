from django.urls import path
from . import views
urlpatterns = [
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



]