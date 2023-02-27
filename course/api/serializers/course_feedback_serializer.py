from rest_framework.serializers import ModelSerializer
from course.api.models.course_feedback import CourseFeedback


class CourseFeedbackSerializer(ModelSerializer):

    class Meta:
        model = CourseFeedback
        fields = "__all__"