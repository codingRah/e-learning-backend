from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from course.api.models.course_part_model import CoursePart
from course.api.serializers.course_part_serializer import CoursePartSerializer
from instructor.api.permission import IsInstructor
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from course.api.serializers.course_attachment_serializer import AttachmentSerializer


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
    
    @action(detail=False, methods=['GET'], url_name='get-all-parts-of-a-course')
    def get_a_course_parts(self, request, *args, **kwargs):
        if request.GET.get('course_id'):
            try:
                all_parts_of_a_course = CoursePart.objects.filter(course_id=request.GET.get('course_id'))
            except CoursePart.DoesNotExist:
                return NotFound("the course doesn't have any comment")
            serializer = CoursePartSerializer(all_parts_of_a_course, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("The course id params not provided!!", status=status.HTTP_406_NOT_ACCEPTABLE)
    
    @action(detail=False, methods=['GET'], url_name='get-all-attachments-of-part')
    def get_all_attachments_of_part(self, request, *args, **kwargs):
        if request.GET.get('part_id'):
            try:
                part = CoursePart.objects.get(pk=request.GET.get('part_id'))
            except CoursePart.DoesNotExist:
                return NotFound("the part doesn't have any attachment!")
            serializer = AttachmentSerializer(part.attachments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("The part id params not provided!!", status=status.HTTP_406_NOT_ACCEPTABLE)