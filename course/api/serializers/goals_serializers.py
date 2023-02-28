from rest_framework import serializers
from course.api.models.goals_model import GoalsModel


class GoalSerializer(serializers.ModelSerializer):
    # pre_course = CourseSerializer(many=True)
    class Meta:
        model = GoalsModel
        fields = ['id', 'title','course_id']