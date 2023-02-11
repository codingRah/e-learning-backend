from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.course_category_view import CourseCategoryView, LanguageView, CourseTypeView
from .views.course_view import CourseView
from .views.enrollment_view import EnrollmentView
from .views.course_part_view import CoursePartView
from .views.course_assignment_view import assignment_list_create_views, assignment_update_delete_views
from .views.comment_views import course_comment_list_create_views,course_comment_update_delete_views


router = DefaultRouter()
router.register('course-category', CourseCategoryView, basename="course-category")
router.register('course-language', LanguageView, basename="course-language")
router.register('course-type', CourseTypeView, basename="course-type")
router.register('course', CourseView, basename="course")
router.register('enrollment', EnrollmentView, basename="course-enrollment")
router.register('course-part', CoursePartView, basename="course-part")
router.register('enrollment', EnrollmentView, basename="course-enrollment")
router.register('assignment-list-create', assignment_list_create_views, basename="assignment-list-create")
router.register('assignment-update-delete', assignment_update_delete_views, basename="assignment-update-delete")
router.register('comment-list-create', course_comment_list_create_views, basename="comment-list-create")
router.register('comment-update-delete', course_comment_update_delete_views, basename="comment-update-delete")


urlpatterns = [
    path('', include(router.urls)),
]
