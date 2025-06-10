from django.urls import path, include
from social_network.settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from .views import FriendsView, AllFriendsView


urlpatterns = [
    path("main/", FriendsView.as_view(), name = "main_friends"),
    path("all_friends/", AllFriendsView.as_view(), name = "all_friends")
]
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)