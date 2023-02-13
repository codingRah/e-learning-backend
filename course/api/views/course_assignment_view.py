from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.decorators import api_view
from course.api.serializers.course_assignment_serializer import CourseAssignmentSerializer
from course.api.models.assignment_model import CourseAssignment


def get_assignment(pk=None):
    try:
        assignment = CourseAssignment.objects.get(pk=pk)
    except:
        raise NotFound(detail="assignment not found")
    return assignment

@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def create_assignment_view(request):
    serializer = CourseAssignmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def get_all_assignment_view(request):
    assignment = CourseAssignment.objects.all()
    serializer = CourseAssignmentSerializer(assignment, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def get_single_assignment_view(request, pk=None):
    assignment = get_assignment(pk=pk)
    serializer = CourseAssignmentSerializer(assignment)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT', ])
@permission_classes((IsAuthenticated, ))
def update_assignment_view(request, pk=None):
    assignment = get_assignment(pk=pk)
    serializer = CourseAssignmentSerializer(data=request.data, instance=assignment)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', ])
@permission_classes((IsAuthenticated, ))    
def delete_assignment_view(request, pk=None):
    assignment = get_assignment(pk=pk)
    assignment.delete()
    return Response({"message": "assignment deleted successfully!"},status=status.HTTP_204_NO_CONTENT)
