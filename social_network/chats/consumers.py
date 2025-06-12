from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .forms import MessageForm


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        text_data_dict = json.loads(text_data)
        form = MessageForm(text_data_dict)
        if form.is_valid():
            await self.send(json.dumps(text_data_dict))

    