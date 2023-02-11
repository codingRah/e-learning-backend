from rest_framework import serializers
from course.api.models.course_video_model import CourseVideo


class CourseVideoSerializer(serializers.Serializer):
    """serializer for course video"""
    name = serializers.FileField()
    video_size = serializers.IntegerField(read_only=True)
    extension = serializers.CharField(read_only=True)
    part = serializers.IntegerField()

    