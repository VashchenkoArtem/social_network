from django.views.generic import TemplateView, FormView
from settings_app.models import Profile, Friendship, Avatar
from .forms import MessageForm
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from .models import ChatGroup, ChatMessage
import json


# Create your views here.
class ChatsView(TemplateView):
    template_name = "all_chats/all_chats.html"

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        response = render(request, self.template_name, context)
        if request.POST.getlist('friends'):  
            checkbox_list = request.POST.getlist('friends')  
            context = self.get_context_data()
            context['selected_friends'] = checkbox_list
            profile = Profile.objects.get(user_id = self.request.user.id)
            group = ChatGroup.objects.create(name = "New Group", admin = profile)
            for people_id in checkbox_list:
                people = Profile.objects.get(id = people_id)
                group.members.add(people)
            group.members.add(profile)
            ids = ""
            for member in group.members.all():
                ids += f" {member.id}"
            ids += " "
            response = render(request, self.template_name, context)
            response.set_cookie('group_members', ids)
            return response
        # else:
        #     request.POST.get("add-image-avatar")
        return response
    def get_context_data(self, **kwargs):
        context = super(ChatsView, self).get_context_data(**kwargs)
        context["all_avatars"] = Avatar.objects.all()
        my_profile = Profile.objects.get(user_id = self.request.user.id)
        context['current_user'] = my_profile
        context["friends"] = Friendship.objects.filter(accepted = True)
        context['all_groups'] = ChatGroup.objects.all()
        context['members_group'] = Profile.objects.filter(user_id = -1)
        if self.request.COOKIES.get('group_members'):
            members_ids = self.request.COOKIES.get('group_members')
            list_ids = str(members_ids).split(" ")
            del list_ids[0]
            del list_ids[-1]
            for id in list_ids:
                profile = Profile.objects.filter(id = id)
                context["members_group"] = context['members_group'].union(profile)
        return context

class ChatView(FormView):
    template_name = "chat/chat.html"
    form_class = MessageForm
    success_url = "/chats/all_chats/chat"
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
        context['times'] = ChatGroup.objects.filter(id = -1)
        list_times = []
        for message_time in all_messages:
            only_time = message_time.sent_at.time()
            list_times.append(only_time)

            print(only_time)
        context['times'] = list_times
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

