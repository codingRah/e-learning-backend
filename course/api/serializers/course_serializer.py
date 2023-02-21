from rest_framework import serializers
from course.api.models.course_model import Course
from accounts.models import User
from course.api.serializers.comment_serializer import CommentSerializer
from django.conf import settings
import os
from datetime import datetime


class CourseSerializer(serializers.ModelSerializer):
    """course serializer"""

    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'category', 'start_date', 'end_date', 'start_time', 'end_time', 'course_type', 'language', 'created_by', 'comments']

        extra_kwargs = {
            'created_by': {'write_only': True}
        }

    def create(self, validated_data):
        course_title = validated_data.pop('title')
        created_user = User.objects.get(pk=validated_data.pop('created_by').id).username
        os.mkdir(os.path.join(settings.MEDIA_ROOT, f'{course_title}-{datetime.now().date()}-{created_user}'))
        return Course.objects.create(**validated_data)