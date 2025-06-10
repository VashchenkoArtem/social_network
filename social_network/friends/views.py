from django.shortcuts import render
from django.views.generic import TemplateView
from settings_app.models import ProfileModel

class FriendsView(TemplateView):
    template_name = "friends/friends.html"

    def get_context_data(self, **kwargs):
        context = super(FriendsView, self).get_context_data(**kwargs)
        user = ProfileModel.objects.get(user = self.request.user)
        context["all_friends"] = user.friends.all()
        return context 
    
class AllFriendsView(TemplateView):
    template_name = "all_friends/all_friends.html"
    def get_context_data(self, **kwargs):
        context = super(AllFriendsView, self).get_context_data(**kwargs)
        user = ProfileModel.objects.get(user = self.request.user)
        context["all_friends"] = user.friends.all()
        return context 