from django.db import models
from accounts.models import User
from user_profile.api.models.student_profile_model import StudentProfile


class Course(models.Model):
    """Course models"""
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    student = models.ManyToManyField(StudentProfile, related_name="courses")
    created_by = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.title}'
