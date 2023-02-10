from rest_framework import serializers
from course.api.models.comments_model import CourseComment



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseComment
        fields = '__all__'



