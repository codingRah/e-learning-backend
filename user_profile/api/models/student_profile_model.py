from django.db import models
from accounts.models import User


class StudentProfile(models.Model):
    """This models will store all information about the students"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=50)
    slug = models.SlugField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user_id}-{self.first_name}'
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
