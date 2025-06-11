from django.shortcuts import render
from django.views.generic import TemplateView
from settings_app.models import ProfileModel, RequestModel

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