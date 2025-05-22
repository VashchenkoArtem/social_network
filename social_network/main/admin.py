from django.contrib import admin
from .models import Tag, User_Post
# Register your models here.


admin.site.register([Tag, User_Post])