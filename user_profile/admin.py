from django.contrib import admin
from .api.models.user_profile_pic_model import UserProfileImage
from .api.models.student_profile_model import StudentProfile


admin.site.register(StudentProfile)
admin.site.register(UserProfileImage)