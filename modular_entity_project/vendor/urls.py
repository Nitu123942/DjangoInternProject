from django.urls import path
from .views import VendorListCreateAPIView, VendorDetailAPIView

urlpatterns = [
    path('vendors/', VendorListCreateAPIView.as_view(), name='vendor-list'),
    path('vendors/<int:pk>/', VendorDetailAPIView.as_view(), name='vendor-detail'),
]