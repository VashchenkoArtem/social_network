from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import PostForm
from .models import User_Post, Pictures
from .forms import PostForm, PostFormEdit
from .models import User_Post
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView


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
 