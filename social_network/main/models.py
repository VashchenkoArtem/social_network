from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    tag_name = models.CharField(max_length = 256, null = True)
    def __str__(self):
        return f"{self.tag_name}"

class User_Post(models.Model):
    user = models.ForeignKey(to = User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 256)
    topic = models.CharField(max_length = 128)
    tags = models.ManyToManyField(Tag)
    text = models.TextField()
    # view_count = models.IntegerField(default = 0)
    views = models.ManyToManyField(User, related_name='view_count', null = True, blank = False)
    like_count = models.IntegerField(default = 0)

class Pictures(models.Model):
    post = models.ForeignKey(User_Post, on_delete = models.CASCADE)
    image = models.ImageField(upload_to= "images/post_images/", null= True)

class Url_Post(models.Model):
    post = models.ForeignKey(User_Post, on_delete = models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return f"{self.url} - {self.post}"