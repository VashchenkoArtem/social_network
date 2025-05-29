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

    class Meta:
        model = User_Post
        fields = ["title", "topic", "tags", "text", "url"]

    images = MultipleField(required=False, label="", widget=MultipleFileInput(attrs={
        "name": "images",
        "id": "image-to-post-form",
        "class": "image-to-post-form",
        "multiple": True 
    }))
    url = forms.URLField(
        required=False,
        label="Посилання",
        widget=forms.URLInput(attrs={
            "placeholder": "Вкажіть посилання до публікації",
            "id": "field-url"
        })
    )

    title = forms.CharField(
        max_length=255,
        label="Назва публікації",
        widget=forms.TextInput(attrs={
            "placeholder": "Напишіть назву публікації",
            "id": "field-title"
        })
    )

    topic = forms.CharField(
        max_length=255,
        required=False,
        label="Тема публікації",
        widget=forms.TextInput(attrs={
            "placeholder": "Напишіть тему публікації",
            "id": "field-topic"
        })
    )

    text = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
            "placeholder": "Напишіть текст публікації",
            "id": "field-text"
        })
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            "id": "field-tags"
        }),
        required=False
    )
    

class PostFormEdit(forms.ModelForm):
    class Meta(PostForm.Meta):
        fields = ["title", "topic", "tags", "text", "url"]

    images = MultipleField(
        required=False,
        label="",
        widget=MultipleFileInput(attrs={
            "id": "image-to-post-form",
            "class": "image-to-post-form",
            "multiple": True
        })
    )

    url = forms.URLField(
        required=False,
        label="Посилання",
        widget=forms.URLInput(attrs={
            "placeholder": "Вкажіть посилання до публікації",
            "id": "field-url"
        })
    )

    title = forms.CharField(
        max_length=255,
        label="Назва публікації",
        widget=forms.TextInput(attrs={
            "placeholder": "Напишіть назву публікації",
            "id": "field-title"
        })
    )

    topic = forms.CharField(
        max_length=255,
        required=False,
        label="Тема публікації",
        widget=forms.TextInput(attrs={
            "placeholder": "Напишіть тему публікації",
            "id": "field-topic"
        })
    )

    text = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
            "placeholder": "Напишіть текст публікації",
            "id": "field-text"
        })
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            "id": "field-tags"
        }),
        required=False
    )