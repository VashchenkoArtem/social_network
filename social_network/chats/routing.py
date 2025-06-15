from django.urls import path
from .consumers import ChatConsumer

ws_urlpatterns = [
    path("chats/all_chats/<int:chat_pk>", ChatConsumer.as_asgi(), name="chat")
]