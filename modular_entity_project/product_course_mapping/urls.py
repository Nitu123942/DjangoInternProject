from django.urls import path
from .views import ProductCourseMappingListCreateAPIView, ProductCourseMappingDetailAPIView

urlpatterns = [
    path('product-course-mappings/', ProductCourseMappingListCreateAPIView.as_view()),
    path('product-course-mappings/<int:pk>/', ProductCourseMappingDetailAPIView.as_view()),
]