from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils import timezone



class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, user_type=None, password=None):
        if not email:
            raise ValueError("Users must have an email address ")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, user_type=user_type)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, user_type=None, password=None):
        user = self.create_user(email, username, user_type, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class UserType(models.Model):
    """this models is for types of models"""
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f'{self.name}'


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username  = models.CharField(max_length=255, unique=True)
    user_type = models.ForeignKey(UserType, on_delete=models.SET_NULL, null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
