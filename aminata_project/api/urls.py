from django.urls import path
from .views import CategoryListView

urlpatterns = [
    path('catalog/', CategoryListView.as_view(), name='category-list-create'),
    # path('catalogs/', CatalogListCreateView.as_view(), name='catalog-list-create'),
    # path('catalogs/<int:pk>/', CatalogDetailView.as_view(), name='catalog-detail'),
]
