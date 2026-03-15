from django.urls import path
from .views import VendorProductMappingListCreateAPIView, VendorProductMappingDetailAPIView

urlpatterns = [
    path('vendor-product-mappings/', VendorProductMappingListCreateAPIView.as_view(), name='vendor-product-mapping-list'),
    path('vendor-product-mappings/<int:pk>/', VendorProductMappingDetailAPIView.as_view(), name='vendor-product-mapping-detail'),
]