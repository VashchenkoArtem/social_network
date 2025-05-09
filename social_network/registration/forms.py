from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import SpecialCode


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email"] 

class VerificationForm(forms.ModelForm):
    class Meta:
        model = SpecialCode
        fields = ["verification_code"]
    