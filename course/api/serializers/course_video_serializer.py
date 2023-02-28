from rest_framework import serializers
from course.api.models.course_video_model import CourseVideo


class CourseVideoSerializer(serializers.ModelSerializer):
    """serializer for course video"""
    
    class Meta:
        model = CourseVideo
        fields = '__all__'
