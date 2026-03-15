from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import VendorProductMapping
from .serializers import VendorProductMappingSerializer
from django.shortcuts import get_object_or_404

# List + Create
class VendorProductMappingListCreateAPIView(APIView):
    def get(self, request):
        mappings = VendorProductMapping.objects.filter(is_active=True)
        serializer = VendorProductMappingSerializer(mappings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VendorProductMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve / Update / Delete
class VendorProductMappingDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(VendorProductMapping, pk=pk, is_active=True)

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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        mapping = self.get_object(pk)
        mapping.is_active = False  # soft delete
        mapping.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
