from django import forms
from .models import User_Post, Tag


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
    images = MultipleField(required = False)

    class Meta:
        model = User_Post
        fields = ["title", "topic", "tags", "text", "url"]
    url = forms.URLField(required = False)