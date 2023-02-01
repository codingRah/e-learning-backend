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


class InstructorListCreateView(generics.ListCreateAPIView):
    queryset = instructor_models.Instructor.objects.all()
    serializer_class = InstructorSerializer


class InstructorUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = instructor_models.Instructor.objects.all()
    serializer_class = InstructorSerializer


class InstructorEducationListCreateView(generics.ListCreateAPIView):
    queryset = instructor_models.InstructorEducation.objects.all()
    serializer_class = InstructorEducationSerializer


class InstructorEducationUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = instructor_models.InstructorEducation.objects.all()
    serializer_class = InstructorEducationSerializer


class InstructorExprienceListCreateView(generics.ListCreateAPIView):
    queryset = instructor_models.InstructorExprience.objects.all()
    serializer_class = InstructorExprienceSerializer


class InstructorExprienceUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = instructor_models.InstructorExprience.objects.all()
    serializer_class = InstructorExprienceSerializer


class InstructorIdCartListCreateView(generics.ListCreateAPIView):
    queryset = instructor_models.InstructorIdCart.objects.all()
    serializer_class = InstructorIdCartSerializer


class InstructorIdCartUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = instructor_models.InstructorIdCart.objects.all()
    serializer_class = InstructorIdCartSerializer


# @api_view()
# def instructor_list_view(request):
#     instructor = instructor_models.Instructor.objects.all()
#     serializer = InstructorSerializer(instructor, many=True)

#     return Response(serializer.data)


# @api_view(["POST"])
# def instructor_create_view(request):

#     serializer = InstructorSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(
#             serializer.data,
#             {"Success": "instructor successfully created"},
#             status=status.HTTP_200_OK,
#         )
#     else:
#         return Response({"Error": "instructor not created"})

# @api_view(['GET','PUT', 'DELETE'])
# def instructor_update_view(request, pk):

#     if request.method == 'GET':
#         try:
#             instructor = instructor_models.Instructor.objects.get(pk=pk)
#         except instructor_models.Instructor.DoesNotExist:
#             return Response({'error': 'the instructor does nor exist'})

#         serializer = InstructorSerializer(instructor)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         instructor = instructor_models.Instructor.objects.get(pk=pk)
#         serializer = InstructorSerializer(instructor, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response({"Error": "instructor not update"}, status=status.HTTP_400_BAD_REQUEST )

#     if request.method == 'DELETE':
#         instructor = instructor_models.Instructor.objects.get(pk=pk)
#         instructor.delete()
#         return Response({'success': 'instructor deleted successfull'})


# class delete_view(generics.RetrieveUpdateDestroyAPIView):
#     queryset = instructor_models.Instructor.objects.all()
#     serializer_class = InstructorSerializer
