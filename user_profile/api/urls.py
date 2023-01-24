from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.user_profile_pic_view import UploadProfileImageViewSet


urlpatterns = [
    path('profile-pic/', UploadProfileImageViewSet, name="profile-pic")
]
