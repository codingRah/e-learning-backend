from rest_framework import serializers
from course.api.models.comments_model import CourseComment


class CommentReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseComment
        fields = ('id', 'body', 'user_id')


class CommentSerializer(serializers.ModelSerializer):

    replied_comments = CommentReplySerializer(many=True, read_only=True)
    class Meta:
        model = CourseComment
        fields = '__all__'
        

class CourseCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseComment
        fields = ('id', 'body', 'user_id', 'course_id')

