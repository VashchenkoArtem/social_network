from django import forms
from .models import User_Post


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleField(forms.ImageField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class PostForm(forms.ModelForm):

    class Meta:
        model = User_Post
        fields = ["title", "topic", "tags", "text", "url"]
    images = MultipleField(required = False,label = "", widget = MultipleFileInput(attrs = {""
    "type": "file",
    "name": "picture",
    "id": "image-to-post-form",
    "class": "image-to-post-form"
    }))
    url = forms.URLField(required = False, label = "Посилання", widget= forms.URLInput(
        {"placeholder": "Вкажіть посилання до публікації"}
    ))
    title = forms.CharField(max_length= 255,label = "Назва публікації", widget= forms.TextInput(
        {"placeholder": "Напишіть назву публікації"}
    ))
    topic = forms.CharField(max_length= 255, required = False,label = "Тема публікації", widget= forms.TextInput(
        {"placeholder": "Напишіть тему публікації"}
    ))
    text = forms.CharField(label = "", widget= forms.Textarea(
        
        {"placeholder": "Напишіть текст публікації"}
    ))
    tags = forms.MultipleChoiceField(required = False)
    


class PostFormEdit(forms.ModelForm):
    images = MultipleField(required = False)
    url = forms.URLField(required = False)
    class Meta(PostForm.Meta):
        fields = ["title", "topic", "tags", "text", "url"]