from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.course_category_view import CourseCategoryView, LanguageView, CourseTypeView
from .views.course_view import CourseView
from .views.enrollment_view import EnrollmentView


router = DefaultRouter()
router.register('course-category', CourseCategoryView, basename="course-category")
router.register('course-language', LanguageView, basename="course-language")
router.register('course-type', CourseTypeView, basename="course-type")
router.register('course', CourseView, basename="course")
router.register('enrollment', EnrollmentView, basename="course-enrollment")


urlpatterns = [
    path('', include(router.urls)),
]
