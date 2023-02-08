from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from course.api.models.course_model import Enrollment
from course.api.serializers.enrollment_serializer import EnrollmentSerializer


class EnrollmentView(ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = EnrollmentSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        enrollment = get_object_or_404(self.queryset, pk=pk)
        serializer = EnrollmentSerializer(enrollment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        enrollment = get_object_or_404(self.queryset, pk=pk)
        serializer = EnrollmentSerializer(enrollment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        enrollment = get_object_or_404(self.queryset, pk=pk)
        serializer = EnrollmentSerializer(enrollment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        enrollment = get_object_or_404(self.queryset, pk=pk)
        enrollment.delete()
        return Response({"message": "Enrollment deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['GET'], url_name="Get My Enrolled Courses", url_path="get-my-enrolled-courses")
    def get_my_enrolled_courses(self, request, pk=None, *args, **kwargs):
        user_id = request.user.id
        try:
            my_courses = Enrollment.objects.filter(student=user_id)
        except:
            raise NotFound("You haven't any enrolled Course")
        serializer = EnrollmentSerializer(my_courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        