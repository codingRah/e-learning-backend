from django.db import models
from .course_model import Course

class PrerequisteModel(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="pre_course", null=True, blank=True)



    def __str__(self) -> str:
        return self.title