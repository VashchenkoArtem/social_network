from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import View
from .forms import PostForm
from .models import User_Post, Pictures, Tag
from .forms import PostForm, PostFormEdit
from settings_app.models import ProfileModel
from .models import User_Post
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserUpdateForm


class MainView(CreateView):
    template_name = "main/index.html"
    form_class = PostForm
    success_url = "/"
    def form_valid(self, form):

        files = self.request.FILES.getlist('images')
        if len(files) > 9:
            form.add_error(None, "Неможливо вказати більше 9 фотографій!")
            return self.form_invalid(form)

        form.instance.user = self.request.user
        response = super().form_valid(form)
        for file in files:
            Pictures.objects.create(post=self.object, image=file)
        return response

    
    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context["posts"] = User_Post.objects.all()
        context["tags"] = Tag.objects.all()
        context['people'] = ProfileModel.objects.get(user_id = self.request.user.pk)
        context['all_peoples'] = ProfileModel.objects.all().exclude(user_id = self.request.user.pk)
        return context 
    
class MyDeleteView(DeleteView):
    template_name = "delete_post/index.html"
    model = User_Post
    success_url = reverse_lazy("main")

class EditView(UpdateView):
    model = User_Post
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
        user_post = [User_Post.objects.get(pk = post_pk)]
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
