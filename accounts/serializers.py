from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from .models import User, UserType



class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            'id', 'email', 'username', 'user_type', 'password'
        )


class UserTypeSerializer(serializers.ModelSerializer):
    """create type of users serializer"""

    class Meta:
        model = UserType
        fields = ['id', 'name']
