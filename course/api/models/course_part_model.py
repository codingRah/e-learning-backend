from django.db import models
from .course_model import Course


class CoursePart(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.course} - {self.title}'
    