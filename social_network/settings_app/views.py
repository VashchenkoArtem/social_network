from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import Avatar, Profile
from .forms import CreateAlbumForm
from publications.models import Album, Image, Tag
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

class UserSettingsView(TemplateView):
    template_name = 'user_settings/user_settings.html'
    def post(self, request, *args, **kwargs):
        profile = Profile.objects.get(user_id = request.user.id)
        avatar = Avatar.objects.filter(profile = profile).first()
        new_name = request.POST.get('username')
        new_avatar = request.FILES.get('avatar')
        if new_avatar:
            if avatar:
                avatar.image = new_avatar
                avatar.save()
            else:
                Avatar.objects.create(profile=profile, image=new_avatar)
        context = self.get_context_data(**kwargs)
        return redirect("user_settings")
    def get_context_data(self, **kwargs):
        context = super(UserSettingsView, self).get_context_data(**kwargs)
        profile = Profile.objects.get(user_id = self.request.user.id)
        context['my_avatar'] = Avatar.objects.filter(profile = profile, shown = True, active = True).first()
        return context
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect("registration") 
        else:   
            return super().dispatch(request, *args, **kwargs)

class UserAlbums(CreateView):
    template_name = 'albums/albums.html'
    form_class = CreateAlbumForm
    success_url = reverse_lazy('albums')
    def get_context_data(self, **kwargs):
        context = super(UserAlbums, self).get_context_data(**kwargs)
        profile = Profile.objects.get(user_id = self.request.user.id)
        context['all_albums'] =  Album.objects.all()
        context['my_avatars'] = Avatar.objects.filter(profile = profile, shown = True, active = True)
        context['all_tags'] = Tag.objects.all()
        try:
            context['album_photos'] = Album.objects.all().first().images.all()
        except:
            print("error")
        return context
    def post(self, request, *args, **kwargs):
        albums_photos = request.FILES.getlist('photos')
        album = Album.objects.all().first()
        for photo in albums_photos:
            picture = Image.objects.create(filename = photo.name, file = photo)
            album.images.add(picture)
        return super().post(request, *args, **kwargs)
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect("registration") 
        else:   
            return super().dispatch(request, *args, **kwargs)

class FriendsView(TemplateView):
    template_name = "friends/friends.html"

class RedactDataView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'user_settings/user_settings.html'
    success_url = reverse_lazy('user_settings')

    def get_object(self, queryset=None):
        return self.request.user

class RedactAlbumView(UpdateView):
    model = Album
    fields = ['name', 'topic']
    template_name = "albums/albums.html"
    success_url = reverse_lazy('albums')

def change_password(request):
    form = PasswordChangeForm(user = request.user, data = request.POST)
    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        return redirect("user_settings")
    return render(request, 'user_settings/user_settings.html', {
        'password_form': form
    })