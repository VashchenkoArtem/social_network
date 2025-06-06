from django.contrib import admin
from django.urls import path
from .views import *
from social_network.settings import MEDIA_URL, MEDIA_ROOT, DEBUG
from django.conf.urls.static import static


urlpatterns = [
    path("user_settings/", UserSettingsView.as_view(), name = "user_settings"),
    path("albums/", UserAlbums.as_view(), name = "albums"),
    path("friends/", FriendsView.as_view(), name = "friends"),
    path("check_info/<int:pk>", RedactDataView.as_view(), name = "check_info")
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)