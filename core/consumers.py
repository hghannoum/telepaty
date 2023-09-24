import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
class YourConsumer(AsyncWebsocketConsumer):
   async def connect(self):

        # Add the client to the group
        await self.channel_layer.group_add(
            "telepaty",
            self.channel_name
        )
        await self.accept()

   async def disconnect(self, close_code):
        # Add your disconnection logic here
        pass
   
   async def receive(self, text_data):
        # Receive a message and broadcast it to the chat room
        message_data = json.loads(text_data)

        await self.channel_layer.group_send(
            "telepaty",
            {
                "type": "chat_message",
                "message": message_data,
            },
        )
        print('baatna')
   async def chat_message(self, event):
        # Send the message to the WebSocket
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))