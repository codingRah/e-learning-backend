from rest_framework import serializers
from course.api.models.course_attachment_model import CourseAttachment



class AttachmentSerializer(serializers.ModelSerializer):

    ALLOWED_EXTENSIONS = ["pdf", "doc", "docx", "pptx", "xls", "xlsx", "txt"]

    def validate_name(self, value):
        file_extension = value.name.split('.')[-1]
        if file_extension not in self.ALLOWED_EXTENSIONS:
            raise serializers.ValidationError("These types of the file not allowed!")
        else: 
            return value

    class Meta:
        model = CourseAttachment
        fields = '__all__'