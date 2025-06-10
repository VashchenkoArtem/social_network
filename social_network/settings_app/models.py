from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from django.contrib.auth import get_user_model
from django.conf import settings

UserModel = get_user_model()

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(auto_now_add=True)
    profile_image = models.ImageField(upload_to= "images/profile_images/", blank = True)
    friends = models.ManyToManyField('self', related_name = "friends", symmetrical=True, blank = True)
    
    def __str__(self):
        return f'{self.user}'