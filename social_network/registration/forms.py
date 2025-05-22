from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import SpecialCode



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length = 256,label = "Електронна пошта", widget = forms.EmailInput(attrs = {
                                                                        "placeholder": "Електронна пошта"
                                                                                }))
    password1 = forms.CharField(max_length= 12,label = "Пароль", widget = forms.PasswordInput(attrs = {
                                                                        "placeholder": "Пароль"
                                                                                }))
    password2 = forms.CharField(max_length= 12,label = "Підтвердити", widget = forms.PasswordInput(attrs = {
                                                                        "placeholder": "Підтвердження пароля"
                                                                                }))
    class Meta:
        model = User
        fields = ["email"] 

class AuthorithationForm(forms.Form):
    email = forms.EmailField(max_length= 256,label = "Пошта")
    password = forms.CharField(widget = forms.PasswordInput)



class VerificationForm(forms.Form):
    input1 = forms.IntegerField(max_value = 9, label = "", widget=forms.NumberInput(attrs = {
        "class": "input1 input",
        "inputmode": "numeric"
    }))
    input2 = forms.IntegerField(max_value = 9, label = "", widget=forms.NumberInput(attrs = {
        "class": "input2 input"
    }))
    input3 = forms.IntegerField(max_value = 9, label = "", widget=forms.NumberInput(attrs = {
        "class": "input3 input"
    }))
    input4 = forms.IntegerField(max_value = 9, label = "", widget=forms.NumberInput(attrs = {
        "class": "input4 input"
    }))
    input5 = forms.IntegerField(max_value = 9, label = "", widget=forms.NumberInput(attrs = {
        "class": "input5 input"
    }))
    input6 = forms.IntegerField(max_value = 9, label = "", widget=forms.NumberInput(attrs = {
        "class": "input6 input"
    }))
    # class Meta:
    #     model = SpecialCode
    #     fields = ["verification_code"]
    
    