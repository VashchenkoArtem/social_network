from django.views.generic import TemplateView, FormView
from settings_app.models import Profile, Friendship, Avatar
from .forms import MessageForm
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from .models import ChatGroup, ChatMessage
import json
from django.urls import reverse


# Create your views here.
class ChatsView(TemplateView):
    template_name = "all_chats/all_chats.html"

    def post(self, request, *args, **kwargs):
        if request.POST.getlist('friends'):  
            selected_ids = request.POST.getlist('friends')
            ids_str = " ".join(selected_ids)
            response = redirect('all_chats') 
            response.set_cookie('group_members', ids_str)
            return response

        else:
            group_name = request.POST.get("group_name")
            group_avatar = request.FILES.get("add-image-avatar")

            ids_str = request.COOKIES.get("group_members", "")
            member_ids = ids_str.strip().split()
            members = Profile.objects.filter(id__in=member_ids)

            group = ChatGroup.objects.create(
                name=group_name,
                avatar=group_avatar,
                admin_id=self.request.user.id
            )
            my_profile = Profile.objects.get(user_id = self.request.user.pk)
            group.members.set(members)
            group.members.add(my_profile)
            

            response = redirect('all_chats')
            response.delete_cookie('group_members')
            return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        my_profile = Profile.objects.get(user_id=self.request.user.id)
        context["all_avatars"] = Avatar.objects.all()
        context["current_user"] = my_profile
        context["friends"] = Friendship.objects.filter(accepted=True)
        context["all_groups"] = ChatGroup.objects.all()
        context["members_group"] = Profile.objects.none()

        ids_str = self.request.COOKIES.get('group_members')
        if ids_str:
            member_ids = ids_str.strip().split()
            context["members_group"] = Profile.objects.filter(id__in=member_ids)
        return context

class ChatView(FormView):
    template_name = "chat/chat.html"
    form_class = MessageForm
    def get_context_data(self, **kwargs):
        context = super(ChatView, self).get_context_data(**kwargs)
        chat_pk = self.kwargs["chat_pk"]
        group = ChatGroup.objects.get(id = chat_pk)
        all_messages = ChatMessage.objects.filter(chat_group = group)

        context['chat_group'] = group
        context["all_avatars"] = Avatar.objects.all()
        context['current_user'] = Profile.objects.get(user_id = self.request.user.id)
        context["friends"] = Friendship.objects.filter(accepted = True)
        context['all_groups'] = ChatGroup.objects.all()
        context['messages'] = all_messages
        # context['times'] = ChatGroup.objects.filter(id = -1)
        # list_times = []
        # for message_time in all_messages:
        #     only_time = message_time.sent_at.time()
        #     list_times.append(only_time)

        #     print(only_time)
        # context['times'] = list_times
        return context
    def get_success_url(self):
        return reverse("chat", kwargs={"chat_pk": self.kwargs["chat_pk"]})
    
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

