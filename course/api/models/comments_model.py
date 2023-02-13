from django.db import models
from accounts.models import User
from .course_model import Course
from .course_video_model import CourseVideo
from .course_attachment_model import CourseAttachment



class CourseComment(models.Model):
    body = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    course_id =models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    video_id = models.ForeignKey(CourseVideo, on_delete=models.CASCADE, null=True, blank=True)
    attachment_id = models.ForeignKey(CourseAttachment, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.body}"
    