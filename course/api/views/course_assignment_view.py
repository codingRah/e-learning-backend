from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view
from course.api.serializers.course_assignment_serializer import CourseAssignmentSerializer
from course.api.models.assignment_model import CourseAssignment


@api_view('GET', 'POST')
def assignment_list_create_views(request):
    if request.method == 'GET':
        assignment = CourseAssignment.objects.all()
        serializer = CourseAssignmentSerializer(assignment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = CourseAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




def assignment_update_delete_views(request, pk):
    if request.method == 'GET':
        assignment = CourseAssignment.objects.get(pk=pk)
        serializer = CourseAssignmentSerializer(assignment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        assignment = CourseAssignment.objects.get(pk=pk)
        serializer = CourseAssignmentSerializer(data=request.data, instance=assignment)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        assignment = CourseAssignment.objects.get(pk=pk)
        assignment.delete()
        return Response({"message": "assignment deleted successfully!"},status=status.HTTP_204_NO_CONTENT)