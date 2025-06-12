from django.contrib import admin
from django.urls import path, include
from social_network.settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path("all_chats/", ChatsView.as_view(), name = "all_chats"),
    path("all_chats/chat", ChatView.as_view(), name = "chat")
]
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)