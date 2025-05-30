from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
# from .models import ProfileModel
# from .forms import ProfileForm


# Create your views here.


class UserSettingsView(TemplateView):
    template_name = 'user_settings/user_settings.html'


class UserAlbums(TemplateView):
    template_name = 'albums/albums.html'

class FriendsView(TemplateView):
    template_name = "friends/friends.html"