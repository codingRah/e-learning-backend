from django.urls import path, include
from .views import user_profile_pic_view
from .views import student_profile_view


urlpatterns = [
    path('std/create/', student_profile_view.create_student_profile, name="create-student-profile"),
    path('std/<slug:slug>/', student_profile_view.student_profile_details, name="student-profile"),
    path('std/update/<slug:slug>/', student_profile_view.update_student_profile, name="update-student-profile"),
    path('std/delete/<slug:slug>/', student_profile_view.delete_student_profile, name="delete-student-profile"),
    path('profile-pic/create/', user_profile_pic_view.create_user_profile, name="create-profile-pic"),
    path('profile-pic/<int:pk>/', user_profile_pic_view.get_user_profile_image, name="get-profile-pic"),
    path('profile-pic/update/<int:pk>/', user_profile_pic_view.update_user_profile_image, name="update-profile-pic"),
    path('profile-pic/delete/<int:pk>/', user_profile_pic_view.delete_user_profile_image, name="delete-profile-pic"),
]

