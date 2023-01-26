from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.views import APIView
from django.conf import settings
import os
from user_profile.api.models.user_profile_pic_model import UserProfileImage
from user_profile.api.serializers.user_profile_pic_serializer import UserProfileImageSerializer



@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@parser_classes((MultiPartParser, FormParser, JSONParser))
def create_user_profile(request):
    """Create new user profile Image"""
    serializer = UserProfileImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def get_user_profile_image(request, pk):
    """Get single user profile image"""
    try:
        user_profile_image = UserProfileImage.objects.get(user=pk)
        serializer = UserProfileImageSerializer(user_profile_image)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response("The user profile image Not Found!", status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', ])
@permission_classes((IsAuthenticated, ))
@parser_classes((MultiPartParser, FormParser, JSONParser))
def update_user_profile_image(request, pk):
    """Update user profile image"""
    user_profile_image = UserProfileImage.objects.get(user=pk)
    os.remove(os.path.join(settings.MEDIA_ROOT, str(user_profile_image.name)))
    serializer = UserProfileImageSerializer(user_profile_image, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['DELETE', ])
@permission_classes((IsAuthenticated, ))
def delete_user_profile_image(request, pk):
    try:
        user_profile_image = UserProfileImage.objects.get(user=pk)
        os.remove(os.path.join(settings.MEDIA_ROOT, str(user_profile_image.name)))
        user_profile_image.delete()
        return Response({"message": "Profile image deleted successfully!"})
    except:
        return Response("The user profile image not found!", status=status.HTTP_400_BAD_REQUEST)

