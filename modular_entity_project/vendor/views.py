from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor
from .serializers import VendorSerializer
from django.shortcuts import get_object_or_404

class VendorListCreateAPIView(APIView):
    def get(self, request):
        vendors = Vendor.objects.filter(is_active=True)
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VendorDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Vendor, pk=pk, is_active=True)

    def get(self, request, pk):
        vendor = self.get_object(pk)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    def put(self, request, pk):
        vendor = self.get_object(pk)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        vendor = self.get_object(pk)
        serializer = VendorSerializer(vendor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        vendor = self.get_object(pk)
        vendor.is_active = False
        vendor.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

