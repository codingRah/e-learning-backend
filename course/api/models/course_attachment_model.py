from django.db import models
from .course_part_model import CoursePart
from .assignment_model import CourseAssignment


class CourseAttachment(models.Model):
    name = models.FileField()
    file_type = models.CharField(max_length=50)
    file_size = models.IntegerField()
    part = models.ForeignKey(CoursePart, on_delete=models.CASCADE)
    assignment = models.ForeignKey(CourseAssignment, on_delete=models.CASCADE, related_name='attachments')

    def __str__(self) -> str:
        return f'{self.name}'
