from rest_framework import serializers
from .models import VendorProductMapping

class VendorProductMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProductMapping
        fields = '__all__'