"""
URL configuration for aminata_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from django.urls import path,include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('api.urls')),
# ]
from django.contrib import admin

from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Payment API",
        default_version='v1',
        description="To help use to get the amount of money that the user has to pay with there name the amount and the payment month",
        terms_of_service="https://www.yourapi.com/terms/",
        contact=openapi.Contact(email="aminatagroup@gmail.com"),
    ))
from django.urls import path
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title="Aminata API",
        default_version='v1',
        description="API documentation for the Aminata project",
        terms_of_service="https://example.com/terms/",
        contact=openapi.Contact(email="contact@aminata.com"),
        license=openapi.License(name="MIT License"),

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # path('user/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('user/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
    path('api/', include('api.urls')),
    # path('payments/',include('payments.urls')),
]
re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),

# from django.urls import path
# from django.urls import path,include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('api.urls')),


from django.urls import include, path

from django.urls import include, path
# fom django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("cart.urls")),
    path('aminata/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('aminata/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),

]


