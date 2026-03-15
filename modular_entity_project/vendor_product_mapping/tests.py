from django.test import TestCase

# Create your tests here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import VendorProductMapping
from .serializers import VendorProductMappingSerializer
from django.shortcuts import get_object_or_404

class VendorProductMappingListCreateAPIView(APIView):
    def get(self, request):
        vendor_id = request.query_params.get('vendor_id', None)
        mappings = VendorProductMapping.objects.all()
        if vendor_id:
            mappings = mappings.filter(vendor_id=vendor_id)
        serializer = VendorProductMappingSerializer(mappings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VendorProductMappingSerializer(data=request.data)
        if serializer.is_valid():
            # Prevent duplicate mapping
            vendor_id = serializer.validated_data['vendor'].id
            product_id = serializer.validated_data['product'].id
            if VendorProductMapping.objects.filter(vendor_id=vendor_id, product_id=product_id).exists():
                return Response({"error": "Duplicate mapping not allowed."}, status=status.HTTP_400_BAD_REQUEST)
            
            # Ensure only one primary mapping per vendor
            if serializer.validated_data.get('primary_mapping', False):
                if VendorProductMapping.objects.filter(vendor_id=vendor_id, primary_mapping=True).exists():
                    return Response({"error": "Primary mapping already exists for this vendor."}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorProductMappingDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(VendorProductMapping, pk=pk)

    def get(self, request, pk):
        mapping = self.get_object(pk)
        serializer = VendorProductMappingSerializer(mapping)
        return Response(serializer.data)

    def put(self, request, pk):
        mapping = self.get_object(pk)
        serializer = VendorProductMappingSerializer(mapping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        mapping = self.get_object(pk)
        serializer = VendorProductMappingSerializer(mapping, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        mapping = self.get_object(pk)
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
