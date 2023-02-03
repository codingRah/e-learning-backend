from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.course_category_view import CourseCategoryView, LanguageView, CourseTypeView
from .views.course_view import CourseView


router = DefaultRouter()
router.register('course-category', CourseCategoryView, basename="course-category")
router.register('course-language', LanguageView, basename="course-language")
router.register('course-type', CourseTypeView, basename="course-type")
router.register('course', CourseView, basename="course")


urlpatterns = [
    path('', include(router.urls)),
]
