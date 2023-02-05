from django.db import models
from .course_part_model import CoursePart


class CourseAttachment(models.Model):
    name = models.FileField(upload_to="course-attachment")
    file_type = models.CharField(max_length=50)
    file_size = models.IntegerField()
    course_chapter = models.ForeignKey(CoursePart, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}'
