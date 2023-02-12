from rest_framework import serializers
from course.api.models.course_model import Course


class CourseSerializer(serializers.ModelSerializer):
    """course serializer"""

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'category', 'start_date', 'end_date', 'start_time', 'end_time', 'course_type', 'language', 'created_by']

        extra_kwargs = {
            'created_by': {'write_only': True}
        }