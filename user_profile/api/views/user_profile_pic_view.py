from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from user_profile.api.models.user_profile_pic_model import UserProfileImage
from user_profile.api.serializers.user_profile_pic_serializer import UserProfileImageSerializer


class UserProfileImageView(APIView):
    
    def get(self, request):
        profile_pic = UserProfileImage.objects.all()
        serializer = UserProfileImageSerializer(profile_pic, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserProfileImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        profile_pic = self.get_object(pk=pk)
        serializer = UserProfileImageSerializer(profile_pic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        profile_pic = self.get_object(pk=pk)
        profile_pic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        try: 
            return UserProfileImage.objects.get(pk=pk)
        except UserProfileImage.DoesNotExist:
            return Response('The Profile image Not found!', status=status.HTTP_404_NOT_FOUND) 

