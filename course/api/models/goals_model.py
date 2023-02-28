from django.db import models
from .course_model import Course

class GoalsModel(models.Model):
    title = models.CharField(max_length=250)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.title