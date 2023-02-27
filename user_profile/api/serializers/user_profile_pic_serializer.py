from rest_framework import serializers
from user_profile.api.models.user_profile_pic_model import UserProfileImage


class UserProfileImageSerializer(serializers.ModelSerializer):
    """serializer for user profile image"""

    def validate_name(value):
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', value)
    class Meta:
        model = UserProfileImage
        fields = ('name', 'user')

        extra_kwargs = {
            'user': {'write_only': True}
        }
