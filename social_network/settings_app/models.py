from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from django.contrib.auth import get_user_model
from django.conf import settings

UserModel = get_user_model()

class RequestModel(models.Model):
    sent_user = models.ForeignKey(User,related_name = "sent_request", on_delete=models.CASCADE, null = True)
    received_user = models.ForeignKey(User,related_name = "received_request", on_delete=models.CASCADE, null = True)
    is_friend = models.BooleanField(default=False)
    

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    date_of_birth = models.DateField(auto_now_add=True)
    profile_image = models.ImageField(upload_to= "images/profile_images/",default = "/../images/account.png", blank = True)
    friends = models.ManyToManyField('self', related_name = "friends", symmetrical=True, blank = True)
    requests = models.ManyToManyField(RequestModel, related_name = "requests", blank = True)
    def remove_friend(self, friend):
        
        if friend in self.friends.all():
            self.friends.remove(friend)
            friend.friends.remove(self)
    def __str__(self):
        return f'{self.user}'
class DeclineRecommended(models.Model):
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='current_user')
    rejected_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rejected_user')