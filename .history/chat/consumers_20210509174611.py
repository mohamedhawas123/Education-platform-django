import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.utils import timezone
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(WebsocketConsumer):

    async def connect(self):
        self.user = self.scope['user']
        self.id = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = 'chat_%s' % self.id

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()
        

    
    async def disconnect(self):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        now = timezone.now()

        await self.channel_layer.group_send(self.room_group_name, {
            'type': 'chat_message',
            'message': message,
            'user': self.user.username,
            'datetime' : now.isoformat(),

        })

        print(self.user.username)



    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))