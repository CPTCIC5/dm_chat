from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from channels.layers import channel_layers


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_group_name="chat"

        user = self.scope['user']
        if not user.is_authenticated:
            return self.close()
        user.is_online = True
        user.save()

        async_to_sync(self.channel_layer.group_add)(self.room_group_name,self.channel_name)
        self.accept()



    # Send the data 
    def chat_message(self, event):
        message = event["message"]
        print('msg0',message)
        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        
        data = {"author":self.scope['user'],"text":message}
        """
        serializer = MessageSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        """
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "data": serializer.data}
        )



    def disconnect(self, code):
        user =self.scope['user']
        user.is_online = False
        user.save()
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name,self.channel_name)