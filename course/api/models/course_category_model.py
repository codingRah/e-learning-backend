from django.db import models


class CourseCategory(models.Model):
    """The course category model"""
    
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.name}'


class CourseType(models.Model):
    """The course type model"""

    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.name}'


class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.name}'