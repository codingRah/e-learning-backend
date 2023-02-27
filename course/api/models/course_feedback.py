from django.db import models
from accounts.models import User
from course.api.models.course_model import Course
from django.core.validators import MaxValueValidator, MinValueValidator


class CourseFeedback(models.Model):
    """feedback the courses"""
    message = models.TextField()
    rate = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(1)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_feedbacks")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user}-{self.rate}'
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'course'], name='unique_user_feedback_to_a_course', violation_error_message="A user can feedback once a coruse")
        ]

