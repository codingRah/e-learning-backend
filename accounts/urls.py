from django.urls import path, include
from .views import RetrieveUpdateDeleteUserType, ListCreateUserType

urlpatterns = [
    path('user-type/<int:pk>/', RetrieveUpdateDeleteUserType.as_view(), name="user-type-retrive-update-delete"),
    path('user-type/', ListCreateUserType.as_view(), name="user-type-create-list"),
]
