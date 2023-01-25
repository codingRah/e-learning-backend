from django.urls import path, include
from .views.user_profile_pic_view import UserProfileImageView
from .views import student_profile_view


urlpatterns = [
    path('std/create/', student_profile_view.create_student_profile, name="create-student-profile"),
    path('std/<slug:slug>/', student_profile_view.student_profile_details, name="student-profile"),
    path('std/update/<slug:slug>/', student_profile_view.update_student_profile, name="update-student-profile"),
    path('std/delete/<slug:slug>/', student_profile_view.delete_student_profile, name="delete-student-profile"),
    path('profile-pic/', UserProfileImageView.as_view(), name="profile-pic"),
]

