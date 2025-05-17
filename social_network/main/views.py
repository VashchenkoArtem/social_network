from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from .forms import PostForm
from .models import User_Post
from django.urls import reverse_lazy


class MainView(CreateView):
    template_name = "main/index.html"
    form_class = PostForm
    success_url = "/"
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context["posts"] = User_Post.objects.all()
            
        return context 
    
class DeleteView(DeleteView):
    template_name = "delete_post/index.html"
    model = User_Post
    success_url = reverse_lazy("main")