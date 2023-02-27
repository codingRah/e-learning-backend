from django.db import models
from .course_part_model import CoursePart
from .course_video_model import CourseVideo


class CourseAssignment(models.Model):

    title = models.CharField(max_length=500)
    description = models.TextField()
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    part_id = models.ForeignKey(CoursePart, on_delete=models.CASCADE, null=True, blank=True)
    video_id = models.ForeignKey(CourseVideo, on_delete=models.CASCADE, null=True, blank=True)
    assignment_response = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.title