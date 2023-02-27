from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.course_category_view import CourseCategoryView, LanguageView, CourseTypeView
from .views.course_view import CourseView
from .views.enrollment_view import EnrollmentView
from .views.course_part_view import CoursePartView
from .views.course_assignment_view import (get_single_assignment_view, 
                                           get_all_assignment_view, 
                                           create_assignment_view, 
                                           update_assignment_view, 
                                           delete_assignment_view)
from .views.comment_views import CourseCommentView
from .views.course_attachment_view import AttachmentView
from .views.course_feedback_view import CourseFeedbackView
from .views.course_video_view import CourseVideoView


router = DefaultRouter()
router.register('course-category', CourseCategoryView, basename="course-category")
router.register('course-language', LanguageView, basename="course-language")
router.register('course-type', CourseTypeView, basename="course-type")
router.register('course', CourseView, basename="course")
router.register('enrollment', EnrollmentView, basename="course-enrollment")
router.register('course-part', CoursePartView, basename="course-part")
router.register('comment', CourseCommentView, basename="course-comment")
router.register('course-video', CourseVideoView, basename="course-video")


urlpatterns = [
    path('', include(router.urls)),
    path('assignment/', include([
        path('', get_all_assignment_view, name="assignment-list"),
        path('create/', create_assignment_view, name="assignment-create"),
        path('<int:pk>/', get_single_assignment_view, name="assignment-details"),
        path('update/<int:pk>/', update_assignment_view, name="assignment-update"),
        path('delete/<int:pk>/', delete_assignment_view, name="assignment-delete"),
    ])),
    path('attachment/', AttachmentView.as_view(), name='attachement'),
    path('attachment/<int:pk>/', AttachmentView.as_view(), name='attachement-details'),
    path('feedback/', CourseFeedbackView.as_view(), name='feedback'),
    path('feedback/<int:pk>/', CourseFeedbackView.as_view(), name='feedback-details'),
]
