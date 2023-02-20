from rest_framework import serializers
from course.api.models.course_model import Course
from course.api.serializers.comment_serializer import CommentSerializer


class CourseSerializer(serializers.ModelSerializer):
    """course serializer"""

    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'category', 'start_date', 'end_date', 'start_time', 'end_time', 'course_type', 'language', 'created_by', 'comments']

        extra_kwargs = {
            'created_by': {'write_only': True}
        }