from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class UserSettingsView(TemplateView):
    template_name = 'user_settings/user_settings.html'