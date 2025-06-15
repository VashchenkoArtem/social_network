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
        context["all_friends"] = Friendship.objects.filter(profile2 = profile, accepted = True)
        context["all_requests"] = Friendship.objects.filter(profile2 = profile, accepted = False)
        return context 
    
    

class AllFriendsView(TemplateView):
    template_name = "all_friends/all_friends.html"
    def get_context_data(self, **kwargs):
        context = super(AllFriendsView, self).get_context_data(**kwargs)
        user = Profile.objects.get(user = self.request.user)
        context["all_friends"] = user.friends.all()
        return context 

class RequestView(TemplateView):
    template_name = "all_requests/requests.html"

    def get_context_data(self, **kwargs):
        context = super(RequestView, self).get_context_data(**kwargs)
        context["all_requests"] = Friendship.objects.filter(received_user = self.request.user.pk)
        return context 
    
class RecommendedView(TemplateView):
    template_name = "recommended/recommended.html"
    def get_context_data(self, **kwargs):
        context = super(RecommendedView, self).get_context_data(**kwargs)
        # all_rejected_pks = DeclineRecommended.objects.filter(
        #                                 current_user=self.request.user
        #                             ).values_list('rejected_user__id', flat=True)
        # all_profiles = Profile.objects.exclude(
        #                                     user_id__in=all_rejected_pks
        #                                 ).exclude(
        #                                     user=self.request.user
        #                                 )
        # context["all_recommended"] = all_profiles
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
    request = Friendship.objects.get(sent_user_id = pk,
                                       received_user = request.user)
    request.delete()
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
    current_user.remove_friend(friend = friend_user)
    return redirect("main_friends")

def confirm_friend(request, pk):    
    current_profile = Profile.objects.get(user_id = request.user.id)
    friend_profile = Profile.objects.get(user_id = pk)
    current_user = User.objects.get(id = request.user.id)
    friend_user = User.objects.get(id = pk)
    current_profile.friends.add(friend_profile)
    request = Friendship.objects.get(sent_user=friend_user, received_user=current_user)
    request.accepted = True
    request.save()
    request.delete()
    return redirect("main_friends")

def request_to_user(request, pk):
    current_user = User.objects.get(id = request.user.id)
    request_user = User.objects.get(id = pk)
    Friendship.objects.create(sent_user = current_user, received_user = request_user, accepted = False)
    return redirect("main_friends")