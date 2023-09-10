from django.urls import path
from .views import UserListView, UserDetailView

urlpatterns = [
    path("user/", UserListView.as_view(), name="user_list_view"),
    path("user/<int:id>/", UserDetailView.as_view(), name="user_detail_view"),
]