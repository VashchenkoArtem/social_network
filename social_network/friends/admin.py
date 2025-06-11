from django.contrib import admin
from settings_app.models import ProfileModel, RequestModel

# Register your models here.

admin.site.register(ProfileModel)
admin.site.register(RequestModel)