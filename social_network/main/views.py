from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import View
from .forms import PostForm
from publications.models import Post,Image, Tag, Link
from .forms import PostForm, PostFormEdit
from settings_app.models import Profile, Friendship, Avatar
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from .forms import UserUpdateForm


class MainView(CreateView):
    template_name = "main/index.html"
    form_class = PostForm
    success_url = "/"
    def form_valid(self, form):
        profile = Profile.objects.get(user_id=self.request.user.pk)
        form.instance.author = profile
        response = super().form_valid(form)
        urls = self.request.POST.getlist('url')   
        for url in urls:
            url = Link.objects.create(post = self.object, url = url) 
        
        files = self.request.FILES.getlist('images')
        for file in files:
            image = Image.objects.create(filename = f"photo-{self.object}", file=file)
            self.object.images.add(image)
        return response

    def dispatch(self, request, *args, **kwargs):
        current_user = Profile.objects.get(user_id = self.request.user.pk)
        user_posts = Post.objects.all()
        if len(user_posts) > 0:
            for post_view in user_posts:
                post_view.views.add(current_user)
                post_view.save()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        context["tags"] = Tag.objects.all()
        context['people'] = Profile.objects.get(user_id = self.request.user.pk)
        context["all_urls"] = Link.objects.all()
        context['all_peoples'] = Profile.objects.all()
        profile = Profile.objects.get(user_id = self.request.user.pk)
        context["posts_count"] = Post.objects.filter(author_id = profile)
        context["my_friends"] = Friendship.objects.filter(profile2 = profile, accepted = True)
        context["all_requests"] = Friendship.objects.filter(profile2 = profile)
        context["all_users"] = Profile.objects.all()
        context["all_avatars"] = Avatar.objects.all()
        context["my_avatars"] = Avatar.objects.filter(profile_id = profile.id)
        return context 
    
class MyDeleteView(DeleteView):
    template_name = "delete_post/index.html"
    model = Post
    success_url = reverse_lazy("main")

class EditView(UpdateView):
    model = Post
    form_class = PostFormEdit
    template_name = 'edit/edit_form.html'
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)
    
class MyLogoutView(LogoutView):
    next_page = reverse_lazy('authorithation')
 
class PostDataView(View):
    def post(self, request, post_pk):
        user_post = [Post.objects.get(pk = post_pk)]
        return JsonResponse(serializers.serialize("json", user_post), safe=False)


class UserUpdateView( UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'main/index.html'
    success_url = reverse_lazy("main")  

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

def check_views(request, pk):
    post = Post.objects.get(id = pk)
    post_views = post.views.all()
    data = {
        'viewsCount': len(post_views)
    }
    return JsonResponse(data)