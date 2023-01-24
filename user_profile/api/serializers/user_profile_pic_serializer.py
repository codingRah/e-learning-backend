from rest_framework import serializers
from user_profile.api.models.user_profile_pic_model import UserProfileImage


class UserProfileImageSerializer(serializers.ModelSerializer):
    """serializer for user profile image"""
    class Meta:
        model = UserProfileImage
        fields = ('name', 'user')