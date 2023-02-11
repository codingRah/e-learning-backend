from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from course.api.models.course_part_model import CoursePart
from course.api.serializers.course_part_serializer import CoursePartSerializer
from instructor.api.permission import IsInstructor


class CoursePartView(viewsets.ModelViewSet):
    """view for course parts"""
    serializer_class = CoursePartSerializer
    queryset = CoursePart.objects.all()
    permission_classes = [IsAuthenticated, IsInstructor | IsAdminUser]

    def list(self, request):
        serializer = CoursePartSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        course_part = get_object_or_404(self.queryset, pk=pk)
        serializer = CoursePartSerializer(course_part)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = CoursePartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        course_part = get_object_or_404(self.queryset, pk=pk)
        serializer = CoursePartSerializer(course_part, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        course_part = get_object_or_404(self.queryset, pk=pk)
        serializer = CoursePartSerializer(course_part, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        course_part = get_object_or_404(self.queryset, pk=pk)
        course_part.delete()
        return Response({"message": "Course part deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)