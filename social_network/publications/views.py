from django.views.generic.edit import CreateView
from main.forms import PostForm
from main.models import User_Post
from django.urls import reverse_lazy


class MyPublicationsView(CreateView):
    template_name = "my_publications/index.html"
    form_class = PostForm
    success_url = reverse_lazy("main")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(MyPublicationsView, self).get_context_data(**kwargs)
        context["posts"] = User_Post.objects.all()
            
        return context 