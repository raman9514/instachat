from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import time
import asyncio
import json

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        group = self.scope["url_route"]["kwargs"]["group_name"]
        await self.channel_layer.group_add(group,self.channel_name)
        

    async def receive(self, text_data=None, bytes_data=None):
        group = self.scope["url_route"]["kwargs"]["group_name"]
        await self.channel_layer.group_send(group,
            {
                "type": "chat.message",
                "text": text_data,
            },
        )
       

    async def disconnect(self, close_code):
        # Called when the socket closes
        group = self.scope["url_route"]["kwargs"]["group_name"]
        self.channel_layer.group_discard(group, self.channel_name)
        await self.close()
    
    async def chat_message(self, event):
        await self.send(text_data=event["text"])