from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from .models import User



class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            'id', 'email', 'username', 'password'
        )