from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from user_profile.api.serializers.student_profile_serializer import StudentProfileSerializer
from user_profile.api.models.student_profile_model import StudentProfile


@api_view(['POST', ])
def create_student_profile(request):
    """Create new student profile"""
    serializer = StudentProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', ])
def student_profile_details(request, pk):
    """Get single student profile information"""
    try:
        student = StudentProfile.objects.get(pk=pk)
        serializer = StudentProfileSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response("The student profile Not Found!", status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
def update_student_profile(request, pk):
    """Update a student profile information"""
    student = StudentProfile.objects.get(pk=pk)
    serializer = StudentProfileSerializer(StudentProfile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['DELETE', ])
def delete_student_profile(request, pk):
    try:
        student = StudentProfile.objects.get(pk=pk)
        student.delete()
        return Response({"message": "Profile info deleted successfully!"})
    except:
        return Response("The student profile not found!", status=status.HTTP_400_BAD_REQUEST)
    