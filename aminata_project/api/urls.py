from django.urls import path, include
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from .views import BookingsListView, BookingsDetailView

# Define the schema view for Swagger documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Catalogue",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
  

    # Your Bookings URLs
    path('Bookings/', BookingsListView.as_view(), name='Bookings-list-view'),  # Changed the name here
    path('Bookings/<int:id>/', BookingsDetailView.as_view(), name='Bookings-detail-view'),  # Changed the name here

    # Swagger documentation
    path('document/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





