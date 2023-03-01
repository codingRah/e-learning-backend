from django.db import models
from .course_part_model import CoursePart
from .course_model import Course
from datetime import datetime
import os


def upload_to_directory(instance, filename):
    course_id = instance.part.course.id if instance.part else None
    if course_id is None:
        raise ValueError("Something Went Wrong!")
    directory = Course.objects.get(pk=course_id).files
    return f'{directory}/videos/{datetime.now().date()}-{filename}'

class CourseVideo(models.Model):
    file_name = models.FileField(upload_to=upload_to_directory)
    video_size = models.IntegerField()
    extension = models.CharField(max_length=50)
    part = models.ForeignKey(CoursePart, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}'