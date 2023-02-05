from django.db import models
from accounts.models import User


class Instructor(models.Model):
    GENDER = (
        ("male", "male"),
        ("female", "female"),
    )
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=GENDER)
    phone = models.CharField(max_length=15)
    dob = models.DateField(null=True, blank=True)
    bio = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="instuctor/image", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class InstructorEducation(models.Model):
    instructor_id = models.ForeignKey(
        Instructor, on_delete=models.CASCADE, related_name="Education"
    )
    title = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    start_date = models.DateField()
    finish_date = models.DateField()
    deploma = models.ImageField(upload_to="instructor_education/deploma")
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.instructor_id.first_name} {self.title}"


class InstructorExprience(models.Model):
    instructor_id = models.ForeignKey(
        Instructor, on_delete=models.CASCADE, related_name="exprience"
    )
    organization = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    finish_date = models.DateField()
    documentation = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.position


class InstructorIdCart(models.Model):
    instructor_id = models.OneToOneField(Instructor, on_delete=models.CASCADE)
    cart_type = models.CharField(max_length=100)
    passport_front = models.ImageField(upload_to="instructor-passport/frant")
    passport_back = models.ImageField(upload_to="instructor-passport/back")
    id_front = models.ImageField(upload_to="instructor-id/front")
    id_back = models.ImageField(upload_to="instructor-id/back")

    def __str__(self) -> str:
        return self.cart_type
