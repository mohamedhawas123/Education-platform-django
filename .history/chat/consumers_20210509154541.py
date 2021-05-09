import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.id = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = 'chat_%s' % self.id

        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)

        self.accept()
        

    
    def disconnect(self):
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(self.room_group_name, {
            'type': 'chat_message',
            'message': 'chat_message'
        })

        print("message")

        self.send(text_data=json.dumps({'message': message}))


    def chat_message(self, event):
        self.send(text_data=json.dumps(event))