# from django import forms
# from .models import ProfileModel
# from django.contrib.auth.models import User


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = ProfileModel
#         fields = ["first_name", "last_name", "username", "email", "password"]
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'profile-input', 'placeholder': "Ім’я"}),
#             'last_name': forms.TextInput(attrs={'class': 'profile-input', 'placeholder': "Прізвище"}),
#             'username': forms.TextInput(attrs={'class': 'profile-input', 'placeholder': "@"}),
#             # 'date_of_birth': forms.DateField(attrs={'class': 'profile-input', 'placeholder': "Дата народження"}),
#             'email': forms.EmailField(max_length = 256,label = "Електронна пошта", widget = forms.EmailInput(attrs = {"placeholder": "Електронна пошта"})),
#             'password': forms.CharField(max_length= 12,label = "Пароль", widget = forms.PasswordInput(attrs = {
#                                                                         "placeholder": "Пароль"
#                                                                                 }))
#         }


# class UpdateProfileForm(ProfileForm):
#     class Meta(ProfileForm.Meta):
#         fields = ["first_name", "last_name", "username", "date_of_birth", "email", "password"]