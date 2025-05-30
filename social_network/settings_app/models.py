from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    date_of_birth = models.DateField(auto_now_add=True)
    profile_image = models.ImageField(upload_to= "images/profile_images/")

    def __str__(self):
        return f'{self.user}: {self.title}'