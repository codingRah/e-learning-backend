from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from course.api.models.goals_model import GoalsModel
from course.api.serializers.goals_serializers import GoalSerializer



class GoalView(ModelViewSet):
    """course view for create, retrieve, update, delete"""
    queryset = GoalsModel.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated,]

    def list(self, request):
        serializer = GoalSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        goal = get_object_or_404(self.queryset, pk=pk)
        serializer = GoalSerializer(goal)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        request.data['created_by'] = request.user.id
        serializer = GoalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        goal = get_object_or_404(self.queryset, pk=pk)
        serializer = GoalSerializer(goal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        goal = get_object_or_404(self.queryset, pk=pk)
        serializer = GoalSerializer(goal, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        goal = get_object_or_404(self.queryset, pk=pk)
        goal.delete()
        return Response({"message": "prerequiste course deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)