from course.api.models.assignment_model import CourseAssignment
from rest_framework import serializers



class CourseAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseAssignment
        fields = '__all__'