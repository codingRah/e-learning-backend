from rest_framework.serializers import ModelSerializer
from course.api.models.course_model import Enrollment


class EnrollmentSerializer(ModelSerializer):

    class Meta:
        model = Enrollment
        fields = '__all__'