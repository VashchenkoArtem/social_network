from django.views.generic import TemplateView, FormView
from settings_app.models import ProfileModel
from .forms import MessageForm
from django.urls import reverse_lazy


# Create your views here.
class ChatsView(TemplateView):
    template_name = "all_chats/all_chats.html"
    def get_context_data(self, **kwargs):
        context = super(ChatsView, self).get_context_data(**kwargs)
        profile = ProfileModel.objects.get(user_id = self.request.user.pk)
        context["my_friends"] = profile.friends.all()
        return context

class ChatView(FormView):
    template_name = "chat/chat.html"
    form_class = MessageForm
    success_url = "/chats/all_chats/chat"

    def get_context_data(self, **kwargs):
        context = super(ChatView, self).get_context_data(**kwargs)
        profile = ProfileModel.objects.get(user_id = self.request.user.pk)
        context["my_friends"] = profile.friends.all()
        return context