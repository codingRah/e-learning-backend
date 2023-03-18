from django.urls import path
from .consumers import NotificationConsumer


websocket_urlpatterns = [
    path('ws/stories/notification_testing/', NotificationConsumer.as_asgi())
]