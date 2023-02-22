from django.db import models
from accounts.models import User
from . course_category_model import CourseCategory, CourseType, Language


class Course(models.Model):
    """Course models"""
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    category = models.ForeignKey(CourseCategory, on_delete=models.SET_NULL, null=True, blank=True)
    course_type = models.ForeignKey(CourseType, on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)
    files = models.CharField(max_length=255, null=True, blank=True)
    enrolleds = models.ManyToManyField(User, through="Enrollment")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="created_by")

    class Meta:
        db_table = 'course_course'
        constraints = [
            models.UniqueConstraint(fields=['title', 'created_by'], name='unique_course_title_for_a_user')
        ]

    def __str__(self) -> str:
        return f'{self.title} - {self.created_at}'


class Enrollment(models.Model):
    """enrollment models"""
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.course} - {self.student} - {self.joined_date}'

