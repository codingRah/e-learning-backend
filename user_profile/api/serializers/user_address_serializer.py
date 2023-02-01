from rest_framework import serializers
from user_profile.api.models.user_address_model import UserAddress, Province


class ProvinceSerializer(serializers.ModelSerializer):
    """province serializer"""
    
    class Meta:
        model = Province
        fields = ('name', 'code')


class UserAddressSerializer(serializers.ModelSerializer):
    """user address serializer"""

    class Meta:
        model = UserAddress
        fields = ('user', 'country', 'province', 'details')
