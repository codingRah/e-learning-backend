from django.db import models


class CourseCategory(models.Model):
    """The course category model"""
    
    name = models.CharField(max_length=255)


class CourseType(models.Model):
    """The course type model"""

    name = models.CharField(max_length=255)


class Language(models.Model):
    name = models.CharField(max_length=255)