from django.db import models
from accounts.models import User


class UserProfileImage(models.Model):
    """this models is to store the user profile pic"""
    name = models.ImageField(upload_to='profile_pc')
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, related_name='profile_pic')

    def __str__(self) -> str:
        return f'{self.name}'
    