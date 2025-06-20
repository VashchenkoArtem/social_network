from django.views.generic.edit import CreateView
from main.forms import PostForm
from .models import Post, Tag
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import TemplateView
from settings_app.models import Profile, Friendship, Avatar
from publications.models import Post,Image, Tag, Link
from django.shortcuts import redirect


class MyPublicationsView(CreateView):
    template_name = "my_publications/index.html"
    form_class = PostForm
    success_url = reverse_lazy("my_pubs")
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
        if not self.request.user.is_authenticated:
            return redirect("registration")
        current_user = Profile.objects.get(user_id = self.request.user.pk)
        user_posts = Post.objects.all()
        if len(user_posts) > 0:
            for post_view in user_posts:
                post_view.views.add(current_user)
                post_view.save()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MyPublicationsView, self).get_context_data(**kwargs)
        profile = Profile.objects.get(user_id = self.request.user.pk)
        context["posts"] = Post.objects.filter(author_id = profile.id)
        context["tags"] = Tag.objects.all()
        context['people'] = Profile.objects.get(user_id = self.request.user.pk)
        context["all_urls"] = Link.objects.all()
        context['all_peoples'] = Profile.objects.all()
        context["posts_count"] = Post.objects.filter(author_id = profile)
        context["my_friends"] = Friendship.objects.filter(profile2 = profile, accepted = True)
        context["all_requests"] = Friendship.objects.filter(profile2 = profile)
        context["all_users"] = Profile.objects.all()
        context["all_avatars"] = Avatar.objects.all()
        context["my_avatars"] = Avatar.objects.filter(profile_id = profile.id)
        return context 
    
 



    
def redact_data(request, post_pk):
    if request.method == 'POST':
        post = [Post.objects.get(id = post_pk)]
        return JsonResponse(serializers.serialize("json", post), safe=False)