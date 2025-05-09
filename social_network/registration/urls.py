from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path("registration", RegistrationView.as_view(), name = "registration"),
    path("confirm", ConfirmRegistrationView.as_view(), name = "confirm"),
    path("authorithation", AuthorizationView.as_view(), name = "authorithation")
]