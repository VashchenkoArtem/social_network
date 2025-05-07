from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]
    special_code = forms.IntegerField(max_value = 999999, required = False)    
    # password = forms.CharField(label="Пароль",widget=forms.PasswordInput)
    # confirm_password = forms.CharField(label="Підтвердження пароля",widget=forms.PasswordInput)
    
    # class Meta:
    #     model = User
    #     fields = ["username","email"]

    # def clean_confirm_password(self):
    #     data = self.cleaned_data
    #     if data.get("password") != data.get("confirm_password"):
    #         raise ValidationError("Паролі не співпадають")
    #     return data