from rest_framework import serializers
from course.api.models.course_model import Course
from course.api.serializers.comment_serializer import CommentSerializer
from course.api.serializers.course_feedback_serializer import CourseFeedbackSerializer
from django.conf import settings

import os
from datetime import datetime


class CourseSerializer(serializers.ModelSerializer):
    """course serializer"""

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("The course title should be more than 5 characters")
        else:
            return value

    def validate_created_by(self, value):
        if value is None:
            raise serializers.ValidationError("something went wrong!")
        else:
            return value
        

    comments = CommentSerializer(many=True, read_only=True)
    course_feedbacks = CourseFeedbackSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'category', 'start_date', 'end_date', 'start_time', 'end_time', \
                  'course_type', 'language', 'created_by', 'comments', 'course_feedbacks']

        extra_kwargs = {
            'created_by': {'write_only': True}
        }

    def create(self, validated_data):
        course_title = validated_data['title']
        created_user = validated_data['created_by'].username
        # try:
        #     os.mkdir(os.path.join(settings.MEDIA_ROOT, f'{course_title}-{datetime.now().date()}-{created_user}'))
        # except OSError as e:
        #     raise serializers.ValidationError("Something went wrong!")
        validated_data['files'] = f'{course_title}-{datetime.now().date()}-{created_user}'
        return Course.objects.create(**validated_data)