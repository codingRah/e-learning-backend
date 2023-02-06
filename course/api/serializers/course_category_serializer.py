from rest_framework import serializers
from course.api.models.course_category_model import CourseCategory, Language, CourseType


class CourseCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseCategory
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = '__all__'


class CourseTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseType
        fields = '__all__'

