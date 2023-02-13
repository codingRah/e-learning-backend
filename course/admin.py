from django.contrib import admin
from .api.models.assignment_model import CourseAssignment
from .api.models.course_model import Course
from .api.models.course_part_model import CoursePart
from .api.models.course_video_model import CourseVideo
from .api.models.course_category_model import CourseCategory, CourseType, Language 
from .api.models.course_attachment_model import CourseAttachment
from .api.models.comments_model import CourseComment



admin.site.register(CourseAssignment)
admin.site.register(Course)
admin.site.register(CourseVideo)
admin.site.register(CourseType)
admin.site.register(CoursePart)
admin.site.register(Language)
admin.site.register(CourseCategory)
admin.site.register(CourseAttachment)
admin.site.register(CourseComment)
