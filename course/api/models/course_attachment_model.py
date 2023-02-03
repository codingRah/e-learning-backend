from django.db import models
from .course_chapter_model import CourseChapter


class CourseAttachment(models.Model):
    name = models.FileField(upload_to="course-attachment")
    file_type = models.CharField(max_length=50)
    file_size = models.IntegerField()
    course_chapter = models.ForeignKey(CourseChapter, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}'
