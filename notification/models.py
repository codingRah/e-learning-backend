from django.db import models
from accounts.models import User


class Notification(models.Model):
    STATUS = (
        ("read", "Read"),
        ("unread", "Unread"),
    )
    user_sender = models.ForeignKey(User, null=True, blank=True, related_name='user_sender' ,on_delete=models.CASCADE)
    user_revoker = models.ForeignKey(User ,null=True ,blank=True ,related_name='user_revoker' ,on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS, default="unread")
    label = models.CharField(max_length=255, default='new notification')
    notification_type = models.CharField(max_length=264, null=True, blank=True)
