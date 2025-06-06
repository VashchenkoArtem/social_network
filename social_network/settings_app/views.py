from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers 
from django.urls import reverse_lazy


class UserSettingsView(TemplateView):
    template_name = 'user_settings/user_settings.html'


class UserAlbums(TemplateView):
    template_name = 'albums/albums.html'

class FriendsView(TemplateView):
    template_name = "friends/friends.html"

class RedactDataView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'user_settings/user_settings.html'
    success_url = reverse_lazy('user_settings')

    def get_object(self, queryset=None):
        return self.request.user