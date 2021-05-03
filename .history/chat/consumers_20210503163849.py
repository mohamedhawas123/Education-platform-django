import json
from channels.generic.websocket import WebsocketConsumer



class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    
    def disconnect(self):
        pass


    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        print("message")

        self.send(text_data=json.dumps({'message': message}))