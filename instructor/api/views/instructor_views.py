from django.shortcuts import render
from instructor.api.serializers.instructor_serializers import (
    InstructorSerializer,
    InstructorEducationSerializer,
    InstructorExperienceSerializer,
    InstructorIdCartSerializer,
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from instructor.api.models import instructor_models
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class InstructorListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = instructor_models.Instructor.objects.all()
    serializer_class = InstructorSerializer


class InstructorUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = instructor_models.Instructor.objects.all()
    serializer_class = InstructorSerializer


class InstructorEducationListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = instructor_models.InstructorEducation.objects.all()
    serializer_class = InstructorEducationSerializer


class InstructorEducationUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = instructor_models.InstructorEducation.objects.all()
    serializer_class = InstructorEducationSerializer


class InstructorExperienceListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = instructor_models.InstructorExperience.objects.all()
    serializer_class = InstructorExperienceSerializer
@api_view(['GET','POST'])
def instructor_experience_list_create_views(request):
    
    if request.method == 'GET':

        instructor = instructor_models.InstructorExperience.objects.all()
        serializer = InstructorExperienceSerializer(instructor, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = InstructorExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def instructor_experience_update_create_views(request, pk):
    if request.method == 'GET':

        instructor = instructor_models.InstructorExperience.objects.all()
        serializer = InstructorExperienceSerializer(instructor, many=True)
        return Response(serializer.data)
    if  request.method == 'PUT':   
        instructor = instructor_models.InstructorExperience.objects.get(pk=pk)
        serializer = InstructorExperienceSerializer(data=request.data, instance=instructor)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    if request.method == 'DELETE':
        instructor = instructor_models.InstructorExperience.objects.get(pk=pk)
        instructor.delete()
        return Response({'success': 'the instructor experience deleted'} , status=status.HTTP_204_NO_CONTENT)


class InstructorExperienceUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = instructor_models.InstructorExperience.objects.all()
    serializer_class = InstructorExperienceSerializer


class InstructorIdCartListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = instructor_models.InstructorIdCart.objects.all()
    serializer_class = InstructorIdCartSerializer


class InstructorIdCartUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = instructor_models.InstructorIdCart.objects.all()
    serializer_class = InstructorIdCartSerializer


