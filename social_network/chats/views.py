from django.views.generic import TemplateView, FormView
from settings_app.models import Profile, Friendship, Avatar
from .forms import MessageForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import ChatGroup, ChatMessage


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
        group = ChatGroup.objects.get(pk = chat_pk)
        context['chat_group'] = group
        context["all_avatars"] = Avatar.objects.all()
        context['current_user'] = Profile.objects.get(user_id = self.request.user.id)
        context["friends"] = Friendship.objects.filter(accepted = True)
        context['all_groups'] = ChatGroup.objects.all()
        context['messages'] = ChatMessage.objects.filter(chat_group = group)

        return context
    
def create_chat(request, user_pk):
    connected_user = Profile.objects.get(pk = user_pk)
    current_user = Profile.objects.get(user_id = request.user.pk)
    user_group_with_us = ChatGroup.objects.filter(members = connected_user, is_personal_chat = True).filter(members =  current_user).first()

    if not user_group_with_us:
        personal_chat = ChatGroup.objects.create(
            name = f"Чат {connected_user} з {current_user}",
            is_personal_chat = True,
            admin_id = current_user.pk
        )
        personal_chat.members.set([current_user, connected_user])
        personal_chat.save()
    else:
        personal_chat = user_group_with_us
    return redirect("chat", personal_chat.pk)