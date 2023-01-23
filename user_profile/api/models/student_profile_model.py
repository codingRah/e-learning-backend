from django.db import models
from accounts.models import User


class StudentProfile(models.Model):
    """This models will store all information about the students"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    profile_pc = models.ImageField(upload_to='Profile_images', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user_id}-{self.first_name}'
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
