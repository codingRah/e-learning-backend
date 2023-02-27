from django.db import models
from .course_part_model import CoursePart
from .assignment_model import CourseAssignment
from .course_model import Course
from datetime import datetime


def upload_to_directory(instance, filename):
    course_id = instance.part.course.id if instance.part else None
    if course_id is None:
        course_id = instance.assignment.part_id.course.id if instance.assignment.part_id else None
        if course_id is None:
            course_id = instance.assignment.video_id.part.course.id
            directory = Course.objects.get(pk=course_id).files
            return f'{directory}/assignments/{datetime.now().date()}-{filename}'
        directory = Course.objects.get(pk=course_id).files
        return f'{directory}/assignments/{datetime.now().date()}-{filename}'
    if course_id is None:
        raise ValueError("Something Went Wrong!")
    directory = Course.objects.get(pk=course_id).files
    return f'{directory}/attachments/{datetime.now().date()}-{filename}'


class CourseAttachment(models.Model):
    name = models.FileField(upload_to=upload_to_directory)
    file_type = models.CharField(max_length=50)
    file_size = models.IntegerField()
    part = models.ForeignKey(CoursePart, on_delete=models.CASCADE, null=True, blank=True)
    assignment = models.ForeignKey(CourseAssignment, on_delete=models.CASCADE, related_name='attachments', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.name}'
    
