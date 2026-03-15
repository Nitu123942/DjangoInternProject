from django.urls import path, include

from modular_entity_project.certification import admin
path('api/', include('vendor.urls')),
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('vendor.urls')),
]