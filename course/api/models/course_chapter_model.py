from django.db import models
from .course_model import Course


class CourseChapter(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    