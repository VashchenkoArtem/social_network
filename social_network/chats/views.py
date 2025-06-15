from django.views.generic import TemplateView, FormView
from settings_app.models import Profile, Friendship, Avatar
from .forms import MessageForm
from django.urls import reverse_lazy
from .models import ChatGroup


# Create your views here.
class ChatsView(TemplateView):
    template_name = "all_chats/all_chats.html"
    def get_context_data(self, **kwargs):
        context = super(ChatsView, self).get_context_data(**kwargs)
        context["all_avatars"] = Avatar.objects.all()
        context['current_user'] = Profile.objects.get(user_id = self.request.user.id)
        context["friends"] = Friendship.objects.filter(accepted = True)
        context['all_groups'] = ChatGroup.objects.all()
        return context

class ChatView(FormView):
    template_name = "chat/chat.html"
    form_class = MessageForm
    success_url = "/chats/all_chats/chat"

    def get_context_data(self, **kwargs):
        context = super(ChatView, self).get_context_data(**kwargs)
        chat_pk = self.kwargs["chat_pk"]
        context['chat_group'] = ChatGroup.objects.get(pk = chat_pk)
        context["all_avatars"] = Avatar.objects.all()
        context['current_user'] = Profile.objects.get(user_id = self.request.user.id)
        context["friends"] = Friendship.objects.filter(accepted = True)
        context['all_groups'] = ChatGroup.objects.all()
        return context