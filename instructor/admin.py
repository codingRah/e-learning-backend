from django.contrib import admin
from instructor.api.models import instructor_models

# Register your models here.

admin.site.register(instructor_models.Instructor)
admin.site.register(instructor_models.InstructorEducation)
