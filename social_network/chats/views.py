from django.views.generic import TemplateView, FormView
from .forms import MessageForm
from django.urls import reverse_lazy


# Create your views here.
class ChatsView(TemplateView):
    template_name = "all_chats/all_chats.html"

class ChatView(FormView):
    template_name = "chat/chat.html"
    form_class = MessageForm
    success_url = "/chats/all_chats/chat"