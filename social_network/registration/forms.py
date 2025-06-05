from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import SpecialCode



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length = 256,label = "Електронна пошта", widget = forms.EmailInput(attrs = {
                                                                        "placeholder": "you@example.com"
                                                                                }))
    password1 = forms.CharField(max_length= 12,label = "Пароль", widget = forms.PasswordInput(attrs = {
                                                                        "placeholder": "Введи пароль"
                                                                                }))
    password2 = forms.CharField(max_length= 12,label = "Підтвердити", widget = forms.PasswordInput(attrs = {
                                                                        "placeholder": "Повтори пароль"
                                                                                }))
    class Meta:
        model = User
        fields = ["email"] 

class AuthorithationForm(forms.Form):
    email = forms.EmailField(max_length= 256,label = "Пошта", widget=forms.EmailInput(attrs ={
        "placeholder": "you@example.com"
    }))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {
        "placeholder": "Введи пароль"
    }), label = "Пароль")



class VerificationForm(forms.Form):
    input1 = forms.CharField(label = "", widget=forms.TextInput(attrs = {
        "class": "input1 input",
        "inputmode": "numeric"
    }))
    input2 = forms.CharField(label = "", widget=forms.TextInput(attrs = {
        "class": "input2 input"
    }))
    input3 = forms.CharField(label = "", widget=forms.TextInput(attrs = {
        "class": "input3 input"
    }))
    input4 = forms.CharField(label = "", widget=forms.TextInput(attrs = {
        "class": "input4 input"
    }))
    input5 = forms.CharField(label = "", widget=forms.TextInput(attrs = {
        "class": "input5 input"
    }))
    input6 = forms.CharField(label = "", widget=forms.TextInput(attrs = {
        "class": "input6 input"
    }))
    
    