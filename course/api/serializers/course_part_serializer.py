from rest_framework.serializers import ModelSerializer
from course.api.models.course_part_model import CoursePart


class CoursePartSerializer(ModelSerializer):

    class Meta:
        model = CoursePart
        fields = '__all__'