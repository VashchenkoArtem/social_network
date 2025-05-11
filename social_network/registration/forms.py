from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import SpecialCode



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length = 256,label = "", widget = forms.EmailInput(attrs = {
                                                                        "placeholder": "Електронна пошта"
                                                                                }))
    password1 = forms.CharField(max_length= 12,label = "", widget = forms.PasswordInput(attrs = {
                                                                        "placeholder": "Пароль"
                                                                                }))
    password2 = forms.CharField(max_length= 12,label = "", widget = forms.PasswordInput(attrs = {
                                                                        "placeholder": "Підтвердження пароля"
                                                                                }))
    class Meta:
        model = User
        fields = ["email"] 

class AuthorithationForm(forms.Form):
    email = forms.EmailField(max_length= 256,label = "Пошта")
    password = forms.CharField(widget = forms.PasswordInput)



class VerificationForm(forms.ModelForm):
    class Meta:
        model = SpecialCode
        fields = ["verification_code"]
    