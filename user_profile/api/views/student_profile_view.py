from rest_framework.response import Response
from rest_framework import viewsets
from user_profile.api.serializers.student_profile_serializer import StudentProfileSerializer
from rest_framework import status
from user_profile.api.models.student_profile_model import StudentProfile


class StudentProfileViewSet(viewsets.ViewSet):
    """view for student profile"""

    def list(self, request):
        pass

    def create(self, request):
        serializer = StudentProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        queryset = StudentProfile.objects.get(pk=pk)
        serializer = StudentProfileSerializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass