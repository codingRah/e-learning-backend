from rest_framework import serializers
from user_profile.api.models.student_profile_model import StudentProfile


class StudentProfileSerializer(serializers.ModelSerializer):
    """serializer for student profile"""

    class Meta:
        model = StudentProfile
        fields = ("user", "first_name", "last_name", "phone", 'gender')
