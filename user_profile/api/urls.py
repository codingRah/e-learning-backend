from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.student_profile_view import StudentProfileViewSet
from .views.user_profile_pic_view import UploadProfileImageViewSet


router = DefaultRouter()
router.register('profile', StudentProfileViewSet, basename="student-profile")

urlpatterns = [
    path('profile-pic/', UploadProfileImageViewSet, name="profile-pic"),
    path('', include(router.urls)),
]

