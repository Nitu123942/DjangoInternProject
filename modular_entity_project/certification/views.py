from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Certification
from .serializers import CertificationSerializer
from django.shortcuts import get_object_or_404

class CertificationListCreateAPIView(APIView):
    def get(self, request):
        certifications = Certification.objects.all()
        serializer = CertificationSerializer(certifications, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CertificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CertificationDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Certification, pk=pk)

    def get(self, request, pk):
        certification = self.get_object(pk)
        serializer = CertificationSerializer(certification)
        return Response(serializer.data)

    def put(self, request, pk):
        certification = self.get_object(pk)
        serializer = CertificationSerializer(certification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        certification = self.get_object(pk)
        serializer = CertificationSerializer(certification, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        certification = self.get_object(pk)
        certification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)