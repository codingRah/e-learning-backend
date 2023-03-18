import json
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync,sync_to_async
from accounts.models import User
from django.contrib.auth.models import AnonymousUser
from .models import Notification


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name='notification'   
        self.room_group_name='notification_group'
        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name)
        await self.accept()
    
    async def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user_sender = await database_sync_to_async(User.objects.get)(pk=2)
        user_revoker = await database_sync_to_async(User.objects.get)(pk=3)
        create_notification = Notification(
            user_sender = user_sender,
            user_revoker = user_revoker,
            label = "a new notification",
            notification_type = 'narmal'
        )
        await database_sync_to_async(create_notification.save)()
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type":"send_notification",
                "message": create_notification.label
            }
        )

    async def disconnect(self,event):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def send_notification(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
