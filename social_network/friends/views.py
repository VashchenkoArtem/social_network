from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DeleteView
from settings_app.models import ProfileModel, RequestModel
from main.models import User_Post
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


class FriendsView(TemplateView):
    template_name = "friends/friends.html"

    def get_context_data(self, **kwargs):
        context = super(FriendsView, self).get_context_data(**kwargs)
        user = ProfileModel.objects.get(user = self.request.user)
        context["all_recommended"] =  ProfileModel.objects.exclude(user_id = self.request.user.pk)
        context["all_friends"] = user.friends.all()
        context["all_requests"] = RequestModel.objects.filter(received_user = self.request.user.pk)
        return context 
    
    

class AllFriendsView(TemplateView):
    template_name = "all_friends/all_friends.html"
    def get_context_data(self, **kwargs):
        context = super(AllFriendsView, self).get_context_data(**kwargs)
        user = ProfileModel.objects.get(user = self.request.user)
        context["all_friends"] = user.friends.all()
        return context 

class RequestView(TemplateView):
    template_name = "all_requests/requests.html"

    def get_context_data(self, **kwargs):
        context = super(RequestView, self).get_context_data(**kwargs)
        context["all_requests"] = RequestModel.objects.filter(received_user = self.request.user.pk)
        return context 
    
class RecommendedView(TemplateView):
    template_name = "recommended/recommended.html"
    def get_context_data(self, **kwargs):
        context = super(RecommendedView, self).get_context_data(**kwargs)
        context["all_recommended"] =  ProfileModel.objects.exclude(user_id = self.request.user.pk)
        return context

class FriendProfileView(TemplateView):
    template_name = 'friend_profile/friend_profile.html'
    def get_context_data(self, **kwargs):
        context = super(FriendProfileView, self).get_context_data(**kwargs)
        friend_pk = self.kwargs['friend_pk']
        context['friend'] = ProfileModel.objects.get(user_id = friend_pk)
        context['all_posts'] = User_Post.objects.filter(user_id = friend_pk)
        return context
        

# class DeleteRequest(DeleteView):
#     template_name = "delete_request/del_request.html"
#     model = RequestModel
#     success_url = reverse_lazy("main_friends")
#     def get_object(self, queryset = None):
#         sent_user_pk = self.kwargs['pk']
#         return get_object_or_404(RequestModel, sent_user_id= 20, received_user_id = 19)
def delete_request(request, pk):
    request = RequestModel.objects.get(sent_user_id = pk,
                                       received_user = request.user)
    request.delete()
    return render(request, "delete_request/del_request.html")