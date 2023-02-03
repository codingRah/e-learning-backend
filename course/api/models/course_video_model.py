from django.db import models
from .course_chapter_model import CourseChapter


class CourseVideo(models.Model):
    name = models.FileField(upload_to="course-video")
    video_size = models.IntegerField()
    video_type = models.CharField(max_length=50)
    chapter = models.ForeignKey(CourseChapter, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}'