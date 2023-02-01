from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.course_category_view import CourseCategoryView, LanguageView, CourseTypeView


router = DefaultRouter()
router.register('course-category', CourseCategoryView, basename="course-category")
router.register('course-language', LanguageView, basename="course-language")
router.register('course-type', CourseTypeView, basename="course-type")


urlpatterns = [
    path('', include(router.urls)),
]
