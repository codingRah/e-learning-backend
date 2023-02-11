from rest_framework import serializers
from course.api.models.course_attachment_model import CourseAttachment



class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseAttachment
        fields = '__all__'