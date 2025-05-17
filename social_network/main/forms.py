from django import forms
from .models import User_Post, Tag


class PostForm(forms.ModelForm):
    class Meta:
        model = User_Post
        fields = ["title", "topic", "tags", "text", "url", "picture"]
    title = forms.CharField(max_length= 256, label = "Назва публікації", widget = forms.TextInput(attrs = {
        "placeholder":"Напишіть назву публікації"
    }))
    topic = forms.CharField(max_length= 128, label = "Тема публікації", widget = forms.TextInput(attrs = {
        "placeholder":"Напишіть тему публікації"
    }))
    url = forms.URLField(label = "Посилання", widget = forms.URLInput(attrs = {
        "placeholder":"Вкажіть посилання до публікації"
    }))
    text = forms.CharField( label = "", widget = forms.Textarea(attrs = {
        "placeholder":"Напишіть текст публікації"
    }))
    picture = forms.ImageField(label = "")
    tags = forms.ModelMultipleChoiceField(queryset = Tag.objects.all(), label = "Хештеги")
