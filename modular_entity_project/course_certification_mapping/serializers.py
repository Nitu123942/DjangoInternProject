from rest_framework import serializers
from .models import CourseCertificationMapping

class CourseCertificationMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCertificationMapping
        fields = '__all__'