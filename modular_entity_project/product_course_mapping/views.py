from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProductCourseMapping
from .serializers import ProductCourseMappingSerializer
from django.shortcuts import get_object_or_404

class ProductCourseMappingListCreateAPIView(APIView):
    def get(self, request):
        product_id = request.query_params.get('product_id', None)
        mappings = ProductCourseMapping.objects.all()
        if product_id:
            mappings = mappings.filter(product_id=product_id)
        serializer = ProductCourseMappingSerializer(mappings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductCourseMappingSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product'].id
            course_id = serializer.validated_data['course'].id
            if ProductCourseMapping.objects.filter(product_id=product_id, course_id=course_id).exists():
                return Response({"error": "Duplicate mapping not allowed."}, status=status.HTTP_400_BAD_REQUEST)

            if serializer.validated_data.get('primary_mapping', False):
                if ProductCourseMapping.objects.filter(product_id=product_id, primary_mapping=True).exists():
                    return Response({"error": "Primary mapping already exists for this product."}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductCourseMappingDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(ProductCourseMapping, pk=pk)

    def get(self, request, pk):
        mapping = self.get_object(pk)
        serializer = ProductCourseMappingSerializer(mapping)
        return Response(serializer.data)

    def put(self, request, pk):
        mapping = self.get_object(pk)
        serializer = ProductCourseMappingSerializer(mapping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        mapping = self.get_object(pk)
        serializer = ProductCourseMappingSerializer(mapping, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        mapping = self.get_object(pk)
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)