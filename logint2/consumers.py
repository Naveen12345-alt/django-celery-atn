import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "notify"
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def send_notification(self, event):
        print("jdshfdhjvndf")
        text_message = event["text"]
        await self.send(json.dumps(text_message))
