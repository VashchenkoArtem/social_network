from django.db import models
from settings_app.models import ProfileModel


# Create your models here.
# class FriendsModel(models.Model):
#     user = models.OneToOneField(to = ProfileModel, on_delete = models.CASCADE)
    

# class Friend_List(models.Model):
#     friend_name = models.ForeignKey(ProfileModel, related_name='name', on_delete=models.CASCADE),
#     is_friend = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username