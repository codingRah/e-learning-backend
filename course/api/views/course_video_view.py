from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from course.api.models.course_video_model import CourseVideo
from course.api.serializers.course_video_serializer import CourseVideoSerializer
from instructor.api.permission import IsInstructor


class CourseVideoView(ModelViewSet):
    """course video view for create, retrieve, update, delete"""
    queryset = CourseVideo.objects.all()
    serializer_class = CourseVideoSerializer
    permission_classes = [IsAuthenticated, IsInstructor | IsAdminUser]

    def list(self, request):
        serializer = CourseVideoSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        course_video = get_object_or_404(self.queryset, pk=pk)
        serializer = CourseVideoSerializer(course_video)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = CourseVideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        course_video = get_object_or_404(self.queryset, pk=pk)
        serializer = CourseVideoSerializer(course_video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        course_video = get_object_or_404(self.queryset, pk=pk)
        serializer = CourseVideoSerializer(course_video, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        course_video = get_object_or_404(self.queryset, pk=pk)
        course_video.delete()
        return Response({"message": "Course Video deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)