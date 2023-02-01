from django.db import models
from .course_chapter_model import CourseChapter


class CourseVideo(models.Model):
    name = models.FileField(upload_to="course-video")
    video_size = models.IntegerField()
    video_type = models.CharField()
    chapter = models.ForeignKey(CourseChapter, on_delete=models.CASCADE)