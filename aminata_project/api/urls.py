from django.urls import path
from .views import CatalogueListView
from .views import CatalogueDetailView




urlpatterns = [
    path('catalogue/', CatalogueListView.as_view(), name='catalogue-list-create'),
    path('catalogue/<int:id>/', CatalogueDetailView.as_view(), name='catalogue-list-create')
]