from django.urls import path
from instructor.api.views import instructor_views

urlpatterns = [
    # url for instructor
    path("create-list/", instructor_views.InstructorListCreateView.as_view()),
    path("update-delete/<str:pk>/", instructor_views.InstructorUpdateDeleteView.as_view()),
    # url for instructor education
    path(
        "education/create-list/",
        instructor_views.InstructorEducationListCreateView.as_view(),
    ),
    path(
        "education/update-delete/<str:pk>/",
        instructor_views.InstructorEducationUpdateDeleteView.as_view(),
    ),
    # url for instructor exprience
    path(
        "experience/create-list/",
        instructor_views.InstructorExperienceListCreateView.as_view(),
    ),
    path(
        "experience/update-delete/<str:pk>/",
        instructor_views.InstructorExperienceUpdateDeleteView.as_view(),
    ),
    # url for instructor IDcart
    path("idcart/create-list/", instructor_views.InstructorIdCartListCreateView.as_view()),
    path(
        "idcart/update-delete/<str:pk>/",
        instructor_views.InstructorIdCartUpdateDeleteView.as_view(),
    ),
]
