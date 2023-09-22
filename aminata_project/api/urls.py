from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('logout_all/', views.user_logout_all, name='user_logout_all'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('farmers/', views.FarmerListView.as_view(), name='user-list'),
    path('farmers/<int:id>/', views.FarmerDetailView.as_view(), name='user-list'),
    path('users/<int:id>/', views.UserDetailView.as_view(), name='user-list'),
    path('suppliers/', views.SupplierListView.as_view(), name='user-list'),
    path('suppliers/<int:id>/', views.SupplierDetailView.as_view(), name='user-list'),

]



from django.urls import path
from .views import BookingsListView, BookingsDetailView

urlpatterns = [ 
    path('Bookings/', BookingsListView.as_view(), name='Bookings_list_view'), 
    path('Bookings/<int:id>/', BookingsDetailView.as_view(), name='Bookings_detail_view'), 
    

]



from django.urls import path,include
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from .views import CatalogueListView
from .views import CatalogueDetailView



schema_view = get_schema_view(
    openapi.Info(
        title="Catalogue",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('catalogue/', CatalogueListView.as_view(), name='catalogue-list-create'),
    path('catalogue/<int:id>/', CatalogueDetailView.as_view(), name='catalogue-list-create'),
    path('document/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



