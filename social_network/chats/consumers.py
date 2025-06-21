from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .forms import MessageForm
from channels.db import database_sync_to_async, sync_to_async
from .models import ChatGroup, ChatMessage
from settings_app.models import Profile, Avatar
from django.core import serializers
from django.http import JsonResponse

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_pk = str(self.scope["url_route"]["kwargs"]["chat_pk"])
        self.group_name = self.chat_pk

        await self.channel_layer.group_add(
            self.group_name, self.channel_name
        )

        await self.accept()
    async def receive(self, text_data):
        self.user = self.scope["user"]
        username = self.user.username
        id = self.user.id
        
        # profile = Profile.objects.get(user_id = id)
        # my_avatar = Avatar.objects.none()
        # for avatar in Avatar.objects.all():
        #     if avatar.profile == profile:
        #         my_avatar = avatar
        #         my_avatar.save()

        # avatars = Avatar.objects.all()
        avatars = await self.get_avatars()
        profile = await self.get_profile()
        saved_message = await self.save_message(message = json.loads(text_data)['message'])
        await self.channel_layer.group_send(self.group_name,
            {
                "type": "send_message_to_chat",
                "text_data": text_data,
                "username": username,
                "date_time": saved_message.sent_at,
                "user_id": id,
                "all_avatars": avatars,
                "profile_id":profile
            })
    async def send_message_to_chat(self, event):
        text_data_dict = json.loads(event['text_data'])
        form = MessageForm(text_data_dict)
        username = event['username']
        text_data_dict['username'] = username
        text_data_dict['date_time'] = event['date_time'].isoformat()
        text_data_dict['user_id'] = event['user_id']
        text_data_dict['all_avatars'] = event['all_avatars']
        text_data_dict['profile_id'] = event['profile_id']
        
        if form.is_valid():
            await self.send(json.dumps(text_data_dict))
            
    @database_sync_to_async
    def save_message(self, message):
        content = message
        author = Profile.objects.get(user = self.scope["user"])
        group = ChatGroup.objects.get(pk = self.group_name)
        return ChatMessage.objects.create(content = content, author = author, chat_group = group)
    @sync_to_async
    def get_avatars(self):
        all_avatars = Avatar.objects.all()
        return json.loads(serializers.serialize("json", all_avatars))
    @sync_to_async
    def get_profile(self):
        self.user = self.scope["user"]
        id = self.user.id
        profile_id = Profile.objects.get(user_id = id)
        return profile_id.id