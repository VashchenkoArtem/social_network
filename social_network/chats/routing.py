from django.urls import path
from .consumers import ChatConsumer

ws_urlpatterns = [
    path("chats/all_chats/chat", ChatConsumer.as_asgi(), name="chat")
]