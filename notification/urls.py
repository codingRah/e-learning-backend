from django.urls import path
from .views import Index


urlpatterns = [
    path('notification/', Index.as_view(), name="index")
]
