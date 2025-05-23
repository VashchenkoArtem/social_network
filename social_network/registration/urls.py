from django.contrib import admin
from django.urls import path
from .views import *
from social_network.settings import MEDIA_URL, MEDIA_ROOT, DEBUG
from django.conf.urls.static import static


urlpatterns = [
<<<<<<< HEAD
    path("registration/", RegistrationView.as_view(), name = "registration"),
    path("confirm/", ConfirmRegistrationView.as_view(), name = "confirm"),
    path("authorithation/", AuthorizationView.as_view(), name = "authorithation")
=======
    path("registration", RegistrationView.as_view(), name = "registration"),
    path("confirm", ConfirmRegistrationView.as_view(), name = "confirm"),
    path("authorithation", AuthorizationView.as_view(), name = "authorithation")
>>>>>>> 005822cbd1572be7aa5eafffa6541d1796475e4e
]
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)