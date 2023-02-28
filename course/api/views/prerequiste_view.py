from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from course.api.models.prerequiste_model import PrerequisteModel
from course.api.serializers.prerequiste_serializer import PrerequisteSerializer



class PrerequisteView(ModelViewSet):
    """course view for create, retrieve, update, delete"""
    queryset = PrerequisteModel.objects.all()
    serializer_class = PrerequisteSerializer
    permission_classes = [IsAuthenticated,]

    def list(self, request):
        serializer = PrerequisteSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        pre_course = get_object_or_404(self.queryset, pk=pk)
        serializer = PrerequisteSerializer(pre_course)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        request.data['created_by'] = request.user.id
        serializer = PrerequisteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        pre_course = get_object_or_404(self.queryset, pk=pk)
        serializer = PrerequisteSerializer(pre_course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        pre_course = get_object_or_404(self.queryset, pk=pk)
        serializer = PrerequisteSerializer(pre_course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        pre_course = get_object_or_404(self.queryset, pk=pk)
        pre_course.delete()
        return Response({"message": "prerequiste course deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)