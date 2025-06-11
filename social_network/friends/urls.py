from django.urls import path, include
from social_network.settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from .views import FriendsView, AllFriendsView, RequestView, RecommendedView


urlpatterns = [
    path("main/", FriendsView.as_view(), name = "main_friends"),
    path("all_friends/", AllFriendsView.as_view(), name = "all_friends"),
    path("all_requests/", RequestView.as_view(), name = "all_requests"),
    path("recommended/", RecommendedView.as_view(), name = "recommended")
]
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)