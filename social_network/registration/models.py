from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SpecialCode(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    verification_code = models.SmallIntegerField(max_length = 6, null = True)