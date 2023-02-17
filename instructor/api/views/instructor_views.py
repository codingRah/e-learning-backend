from django.shortcuts import render
from instructor.api.serializers.instructor_serializers import (
    InstructorSerializer,
    InstructorEducationSerializer,
    InstructorExprienceSerializer,
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


class InstructorExprienceListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = instructor_models.InstructorExprience.objects.all()
    serializer_class = InstructorExprienceSerializer


@api_view(['GET','POST'])
def instructor_exprience_list_create_views(request):
    
    if request.method == 'GET':

        instructor = instructor_models.InstructorExprience.objects.all()
        serializer = InstructorExprienceSerializer(instructor, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = InstructorExprienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def instructor_exprience_update_create_views(request, pk):
    if request.method == 'GET':

        instructor = instructor_models.InstructorExprience.objects.all()
        serializer = InstructorExprienceSerializer(instructor, many=True)
        return Response(serializer.data)
    if  request.method == 'PUT':   
        instructor = instructor_models.InstructorExprience.objects.get(pk=pk)
        serializer = InstructorExprienceSerializer(data=request.data, instance=instructor)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    if request.method == 'DELETE':
        instructor = instructor_models.InstructorExprience.objects.get(pk=pk)
        instructor.delete()
        return Response({'success': 'the instructor exprience deleted'} , status=status.HTTP_204_NO_CONTENT)


class InstructorExprienceUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = instructor_models.InstructorExprience.objects.all()
    serializer_class = InstructorExprienceSerializer


class InstructorIdCartListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = instructor_models.InstructorIdCart.objects.all()
    serializer_class = InstructorIdCartSerializer


class InstructorIdCartUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = instructor_models.InstructorIdCart.objects.all()
    serializer_class = InstructorIdCartSerializer


