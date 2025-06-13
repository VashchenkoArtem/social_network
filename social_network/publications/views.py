from django.views.generic.edit import CreateView
from main.forms import PostForm
from main.models import User_Post, Tag
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import TemplateView
from settings_app.models import ProfileModel, RequestModel


class MyPublicationsView(CreateView):
    template_name = "my_publications/index.html"
    form_class = PostForm
    success_url = reverse_lazy("my_pubs")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        current_user = self.request.user.pk
        user_posts = User_Post.objects.all()
        
        for post_view in user_posts:
            post_view.views.add(current_user)
            post_view.save()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(MyPublicationsView, self).get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context['people'] = ProfileModel.objects.get(user_id = self.request.user.pk)
        context['my_posts'] = User_Post.objects.filter(user_id = self.request.user.pk)
        context['all_peoples'] = ProfileModel.objects.all()
        context["posts_count"] = User_Post.objects.filter(user_id = self.request.user.pk)
        profile = ProfileModel.objects.get(user_id = self.request.user.pk)
        context["my_friends"] = profile.friends
        context["all_requests"] = RequestModel.objects.filter(received_user = self.request.user.pk)
        
 

        return context 
        # context = super(MyPublicationsView, self).get_context_data(**kwargs)
        # context["posts"] = User_Post.objects.all()
        # context["tags"] = Tag.objects.all()
            
        # return context 


    
def redact_data(request, post_pk):
    if request.method == 'POST':
        post = [User_Post.objects.get(id = post_pk)]
        return JsonResponse(serializers.serialize("json", post), safe=False)