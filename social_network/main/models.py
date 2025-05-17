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
    url = models.URLField(null = True, blank = False)
    view_count = models.IntegerField(default = 0)
    like_count = models.IntegerField(default = 0)
    picture = models.ImageField(upload_to="images/post_images", null = True, blank = True)
    def __str__(self):
        return f'{self.user}: {self.title}'

    