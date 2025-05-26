from django.contrib import admin
from django.urls import path
from .views import *
from social_network.settings import MEDIA_URL, MEDIA_ROOT, DEBUG
from django.conf.urls.static import static


urlpatterns = [
    path("user_settings/", UserSettingsView.as_view(), name = "user_settings"),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)