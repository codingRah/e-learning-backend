from django.urls import path
from instructor.api.views import instructor_views

urlpatterns = [
    # url for instructor
    path("create/", instructor_views.InstructorListCreateView.as_view()),
    path("update/<str:pk>/", instructor_views.InstructorUpdateDeleteView.as_view()),
    # url for instructor education
    path(
        "education/create/",
        instructor_views.InstructorEducationListCreateView.as_view(),
    ),
    path(
        "education/update/<str:pk>/",
        instructor_views.InstructorEducationUpdateDeleteView.as_view(),
    ),
    # url for instructor exprience
    path(
        "exprience/create/",
        instructor_views.InstructorExprienceListCreateView.as_view(),
    ),
    path(
        "exprience/update/<str:pk>/",
        instructor_views.InstructorExprienceUpdateDeleteView.as_view(),
    ),
    # url for instructor IDcart
    path("idcart/create/", instructor_views.InstructorIdCartListCreateView.as_view()),
    path(
        "idcart/update/<str:pk>/",
        instructor_views.InstructorIdCartUpdateDeleteView.as_view(),
    ),
]
