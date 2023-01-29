from django.db import models
from accounts.models import User


class Province(models.Model):
    """all province"""
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    code = models.CharField(max_length=50, unique=True, null=True, blank=True)

class UserAddress(models.Model):
    """store the address of users"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    country = models.CharField(max_length=255, unique=True, null=False)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    details = models.CharField(max_length=255, null=True, blank=True)
