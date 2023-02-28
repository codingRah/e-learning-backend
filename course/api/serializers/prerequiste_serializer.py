from rest_framework import serializers
from course.api.models.prerequiste_model import PrerequisteModel
from .course_serializer import CourseSerializer
from course.api.models.course_model import Course

class PrerequisteSerializer(serializers.ModelSerializer):
    # pre_course = CourseSerializer(many=True)
    class Meta:
        model = PrerequisteModel
        fields = ['id', 'title','course_id']


    # def create(self, validated_data):
    #     course = validated_data.pop("pre_course")
    #     pre_course = PrerequisteModel.objects.create(**validated_data)
    #     pre_course.title = pre_course.title
    #     for pre in course: 
    #         i = Course.objects.create(pre_course=pre_course, **pre)
    #     return pre_course
