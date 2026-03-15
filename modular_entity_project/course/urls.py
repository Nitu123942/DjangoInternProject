from django.urls import path
from .views import CourseListCreateAPIView, CourseDetailAPIView

urlpatterns = [
    path('courses/', CourseListCreateAPIView.as_view()),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view()),
]