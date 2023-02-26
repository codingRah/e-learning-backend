from django.db import models
from .course_part_model import CoursePart
from .assignment_model import CourseAssignment


def upload_to_directory(instance, filename):
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', instance)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', filename)

class CourseAttachment(models.Model):
    name = models.FileField(upload_to=upload_to_directory)
    file_type = models.CharField(max_length=50)
    file_size = models.IntegerField()
    part = models.ForeignKey(CoursePart, on_delete=models.CASCADE, null=True, blank=True)
    assignment = models.ForeignKey(CourseAssignment, on_delete=models.CASCADE, related_name='attachments', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.name}'
    
