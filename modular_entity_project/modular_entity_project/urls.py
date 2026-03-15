from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Modular Entity Project!")
schema_view = get_schema_view(
   openapi.Info(
      title="Modular Entity API",
      default_version='v1',
      description="Django Intern Assignment APIs using APIView",
      terms_of_service="https://www.example.com/terms/",
      contact=openapi.Contact(email="nitusupport@example.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
"""
URL configuration for modular_entity_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('vendor_product_mapping.urls')),
    path('api/', include('vendor.urls')),
    path('api/', include('product_course_mapping.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # Ye add karo:
    path('', home),  # <-- home page

    path('admin/', admin.site.urls),
    
    # Master apps
    path('api/', include('vendor.urls')),
    path('api/', include('product.urls')),
    path('api/', include('course.urls')),
    path('api/', include('certification.urls')),

    # Mapping apps
    path('api/', include('vendor_product_mapping.urls')),
    path('api/', include('product_course_mapping.urls')),
    path('api/', include('course_certification_mapping.urls')),

    # Swagger & ReDoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

