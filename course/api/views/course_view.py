from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from course.api.models.course_model import Course
from course.api.serializers.course_serializer import CourseSerializer
from instructor.api.permission import IsInstructor
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from course.api.serializers.course_part_serializer import CoursePartSerializer


class CourseView(ModelViewSet):
    """course view for create, retrieve, update, delete"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsInstructor | IsAdminUser]

    def list(self, request):
        serializer = CourseSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        course = get_object_or_404(self.queryset, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        request.data['created_by'] = request.user.id
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        course = get_object_or_404(self.queryset, pk=pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        course = get_object_or_404(self.queryset, pk=pk)
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        course = get_object_or_404(self.queryset, pk=pk)
        course.delete()
        return Response({"message": "Course deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=False, methods=['GET'], url_name='get-all-parts-of-course')
    def get_course_parts(self, request, *args, **kwargs):
        if request.GET.get('course_id'):
            try:
                course = Course.objects.get(pk=int(request.GET.get('course_id')))
            except Course.DoesNotExist:
                return NotFound("Course not found")
            serializer = CoursePartSerializer(course.parts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("The course id params not provided!!", status=status.HTTP_406_NOT_ACCEPTABLE)