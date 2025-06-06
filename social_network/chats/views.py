from django.views.generic import TemplateView

# Create your views here.
class ChatsView(TemplateView):
    template_name = "all_chats/all_chats.html"