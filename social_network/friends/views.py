from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DeleteView
from settings_app.models import Profile, Friendship, Avatar
from publications.models import Post
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


class FriendsView(TemplateView):
    template_name = "friends/friends.html"
    def get_context_data(self, **kwargs):
        context = super(FriendsView, self).get_context_data(**kwargs)
        profile = Profile.objects.get(user = self.request.user)
        context["all_recommended"] = Profile.objects.filter().exclude(user = self.request.user)
        context["all_friends"] = Friendship.objects.filter(accepted = True)
        context["all_requests"] = Friendship.objects.filter(profile2 = profile, accepted = False)
        context["all_avatars"] = Avatar.objects.all()
        context["current_user"] = Profile.objects.get(user = self.request.user)
        return context 
    
    

class AllFriendsView(TemplateView):
    template_name = "all_friends/all_friends.html"
    def get_context_data(self, **kwargs):
        context = super(AllFriendsView, self).get_context_data(**kwargs)
        context["all_friends"] = Friendship.objects.filter(accepted = True)
        context["all_avatars"] = Avatar.objects.all()
        context["current_user"] = Profile.objects.get(user = self.request.user)
        return context 

class RequestView(TemplateView):
    template_name = "all_requests/requests.html"

    def get_context_data(self, **kwargs):
        context = super(RequestView, self).get_context_data(**kwargs)
        profile = Profile.objects.get(user = self.request.user)
        context["all_requests"] = Friendship.objects.filter(profile2 = profile, accepted = False)
        context["all_avatars"] = Avatar.objects.all()
        return context 
    
class RecommendedView(TemplateView):
    template_name = "recommended/recommended.html"
    def get_context_data(self, **kwargs):
        context = super(RecommendedView, self).get_context_data(**kwargs)
        context["all_recommended"] = Profile.objects.filter().exclude(user = self.request.user)
        context["all_avatars"] = Avatar.objects.all()
        return context

class FriendProfileView(TemplateView):
    template_name = 'friend_profile/friend_profile.html'
    def get_context_data(self, **kwargs):
        context = super(FriendProfileView, self).get_context_data(**kwargs)
        friend_pk = self.kwargs['friend_pk']
        friend_user = User.objects.get(id = friend_pk)
        profile_id = Profile.objects.get(user_id = friend_pk)
        context['friend'] = Profile.objects.get(user_id = friend_pk)
        context['avatar'] = Avatar.objects.filter(profile = profile_id)
        context['all_avatars'] = Avatar.objects.all()
        context['all_posts'] = Post.objects.filter(author_id = profile_id.pk).all()

        context['current_request'] = Friendship.objects.get(profile1= Profile.objects.get(user = friend_user), profile2 =Profile.objects.get(user = self.request.user))
        return context
        

def delete_request(request, pk):
    current_user = Profile.objects.get(user_id = request.user.id)
    friend_user = Profile.objects.get(user_id = pk)
    if Friendship.objects.filter(profile1_id = request.user.pk, profile2 = friend_user):
        Friendship.objects.get(profile1 = current_user, profile2 = friend_user).delete()
    if Friendship.objects.filter(profile2 = current_user, profile1 = friend_user):
        Friendship.objects.get(profile2 = current_user, profile1 = friend_user).delete()
    return redirect("main_friends")

def delete_recommended(request, pk):
    rejected_user = User.objects.get(id = pk)
    # DeclineRecommended.objects.get_or_create(
    #             current_user=request.user,
    #             rejected_user=rejected_user
    #         )
    return redirect("main_friends")

def delete_friend(request, pk):
    current_user = Profile.objects.get(user_id = request.user.id)
    friend_user = Profile.objects.get(user_id = pk)
    if Friendship.objects.filter(profile1 = current_user, profile2 = friend_user):
        Friendship.objects.get(profile1 = current_user, profile2 = friend_user).delete()
    if Friendship.objects.filter(profile2 = current_user, profile1 = friend_user):
        Friendship.objects.get(profile2 = current_user, profile1 = friend_user).delete()
    return redirect("main_friends")

def confirm_friend(request, pk):    
    current_profile = Profile.objects.get(user_id = request.user.id)
    friend_profile = Profile.objects.get(user_id = pk)
    current_user = User.objects.get(id = request.user.id)
    friend_user = User.objects.get(id = pk)
    request = Friendship.objects.get(profile1=friend_profile, profile2=current_profile)
    request.accepted = True
    request.save()
    return redirect("main_friends")

def request_to_user(request, pk):
    current_user = Profile.objects.get(user_id = request.user.id)
    request_user = Profile.objects.get(user_id = pk)
    Friendship.objects.create(profile1 = current_user, profile2 = request_user, accepted = False)
    return redirect("main_friends")