from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
# from .models import ProfileModel
# from .forms import ProfileForm


# Create your views here.


class UserSettingsView(TemplateView):
    template_name = 'user_settings/user_settings.html'


class UserAlbums(TemplateView):
    template_name = 'user_settings/albums.html'

# class UserSettingsView(UpdateView):
#     model = ProfileModel
#     form_class = ProfileForm
#     template_name = 'user_settings/user_settings.html'

#     def form_valid(self, form):
#         form.instance.user = self.request.user  
#         return super().form_valid(form)
