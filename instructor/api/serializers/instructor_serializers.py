from rest_framework import serializers
from instructor.api.models.instructor_models import (
    Instructor,
    InstructorIdCart,
    InstructorEducation,
    InstructorExprience,
)


class InstructorEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorEducation
        fields = "__all__"



class InstructorExprienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorExprience
        fields = "__all__"


class InstructorSerializer(serializers.ModelSerializer):
    Education = InstructorEducationSerializer(many=True, read_only=True)
    exprience = InstructorExprienceSerializer(many=True,read_only=True)
    class Meta:
        model = Instructor
        fields = "__all__"


class InstructorIdCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorIdCart
        fields = "__all__"
