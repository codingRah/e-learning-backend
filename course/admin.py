from django.contrib import admin
from .api.models import assignment_model, course_attachment_model, comments_model,course_category_model, course_model, course_part_model,course_video_model


admin.site.register(assignment_model.CourseAssignment)
admin.site.register(course_attachment_model.CourseAttachment)
admin.site.register(comments_model.CourseComment)
admin.site.register(course_category_model.CourseCategory)
admin.site.register(course_model.Course)
admin.site.register(course_part_model.CoursePart)
admin.site.register(course_video_model.CourseVideo)