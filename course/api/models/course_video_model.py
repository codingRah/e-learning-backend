from django.db import models
from .course_part_model import CoursePart


class CourseVideo(models.Model):
    name = models.FileField(upload_to="course-video")
    video_size = models.IntegerField()
    extension = models.CharField(max_length=50)
    part = models.ForeignKey(CoursePart, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}'