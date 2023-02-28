from django.contrib import admin
from .api.models.assignment_model import CourseAssignment
from .api.models.course_model import Course
from .api.models.course_part_model import CoursePart
from .api.models.course_video_model import CourseVideo
from .api.models.course_category_model import CourseCategory, CourseType, Language 
from .api.models.course_attachment_model import CourseAttachment
from .api.models.comments_model import CourseComment
from .api.models.prerequiste_model import PrerequisteModel
from .api.models.goals_model import GoalsModel



admin.site.register(CourseAssignment)
admin.site.register(Course)
admin.site.register(CourseVideo)
admin.site.register(CourseType)
admin.site.register(CoursePart)
admin.site.register(Language)
admin.site.register(CourseCategory)
admin.site.register(CourseAttachment)
admin.site.register(CourseComment)
admin.site.register(PrerequisteModel)
admin.site.register(GoalsModel)
