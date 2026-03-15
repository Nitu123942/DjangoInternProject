from rest_framework import serializers
from .models import ProductCourseMapping

class ProductCourseMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCourseMapping
        fields = '__all__'