from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from user_profile.api.serializers.user_profile_pic_serializer import UserProfileImageSerializer


class UploadProfileImageViewSet(mixins.CreateModelMixin, 
                                mixins.RetrieveModelMixin, 
                                mixins.UpdateModelMixin, 
                                mixins.DestroyModelMixin):
    serializer_class = UserProfileImageSerializer
    # permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return super().get_queryset()
    