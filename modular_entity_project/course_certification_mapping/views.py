from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CourseCertificationMapping
from .serializers import CourseCertificationMappingSerializer
from django.shortcuts import get_object_or_404

class CourseCertificationMappingListCreateAPIView(APIView):
    def get(self, request):
        course_id = request.query_params.get('course_id', None)
        mappings = CourseCertificationMapping.objects.all()
        if course_id:
            mappings = mappings.filter(course_id=course_id)
        serializer = CourseCertificationMappingSerializer(mappings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseCertificationMappingSerializer(data=request.data)
        if serializer.is_valid():
            course_id = serializer.validated_data['course'].id
            cert_id = serializer.validated_data['certification'].id
            if CourseCertificationMapping.objects.filter(course_id=course_id, certification_id=cert_id).exists():
                return Response({"error": "Duplicate mapping not allowed."}, status=status.HTTP_400_BAD_REQUEST)

            if serializer.validated_data.get('primary_mapping', False):
                if CourseCertificationMapping.objects.filter(course_id=course_id, primary_mapping=True).exists():
                    return Response({"error": "Primary mapping already exists for this course."}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseCertificationMappingDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(CourseCertificationMapping, pk=pk)

    def get(self, request, pk):
        mapping = self.get_object(pk)
        serializer = CourseCertificationMappingSerializer(mapping)
        return Response(serializer.data)

    def put(self, request, pk):
        mapping = self.get_object(pk)
        serializer = CourseCertificationMappingSerializer(mapping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        mapping = self.get_object(pk)
        serializer = CourseCertificationMappingSerializer(mapping, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        mapping = self.get_object(pk)
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)