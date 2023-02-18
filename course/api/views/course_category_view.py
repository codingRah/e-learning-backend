from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from course.api.serializers.course_category_serializer import CourseCategorySerializer, LanguageSerializer, CourseTypeSerializer
from course.api.models.course_category_model import CourseCategory, Language, CourseType


class CourseCategoryView(viewsets.ModelViewSet):
    """view for course categories"""
    serializer_class = CourseCategorySerializer
    queryset = CourseCategory.objects.all()
    permission_classes = (IsAuthenticated, )

    def list(self, request):
        serializer = CourseCategorySerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        course_category = get_object_or_404(self.queryset, pk=pk)
        serializer = CourseCategorySerializer(course_category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = CourseCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        course_category = get_object_or_404(self.queryset, pk=pk)
        serializer = CourseCategorySerializer(course_category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        course_category = get_object_or_404(self.queryset, pk=pk)
        serializer = CourseCategorySerializer(course_category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        course_category = get_object_or_404(self.queryset, pk=pk)
        course_category.delete()
        return Response({"message": "Course category deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)


class LanguageView(viewsets.ModelViewSet):
    """view for course languages"""
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
    permission_classes = (IsAuthenticated, )

    def list(self, request):
        serializer = LanguageSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        language = get_object_or_404(self.queryset, pk=pk)
        serializer = LanguageSerializer(language)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        language = get_object_or_404(self.queryset, pk=pk)
        serializer = LanguageSerializer(language, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        language = get_object_or_404(self.queryset, pk=pk)
        serializer = LanguageSerializer(language, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        language = get_object_or_404(self.queryset, pk=pk)
        language.delete()
        return Response({"message": "Language deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)


class CourseTypeView(viewsets.ModelViewSet):
    """view for course Types"""
    serializer_class = CourseTypeSerializer
    queryset = CourseType.objects.all()
    permission_classes = (IsAuthenticated, )

    def list(self, request):
        serializer = CourseTypeSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        course_type = get_object_or_404(self.queryset, pk=pk)
        serializer = CourseTypeSerializer(course_type)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = CourseTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        course_type = get_object_or_404(self.queryset, pk=pk)
        serializer = CourseTypeSerializer(course_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        course_type = get_object_or_404(self.queryset, pk=pk)
        serializer = CourseTypeSerializer(course_type, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        course_type = get_object_or_404(self.queryset, pk=pk)
        course_type.delete()
        return Response({"message": "Course Type deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
