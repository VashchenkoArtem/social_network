from django.views.generic.edit import CreateView, FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import RegistrationForm
from .forms import VerificationForm, AuthorithationForm
from django.core.mail import send_mail
import random
from django.contrib.auth.models import User
from settings_app.models import Profile, VerificationCode
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = "registration/index.html"
    success_url = reverse_lazy("confirm")
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        if not User.objects.filter(email = email).exists():
            return super().post(request, *args, **kwargs)
        else:
            return redirect("registration")
    def form_valid(self, form):
        response = super().form_valid(form)
        response.set_cookie('email', form.cleaned_data['email'], max_age=3600)
        special_code = random.randint(99999, 999999)
        user_id = User.objects.get(email = form.cleaned_data['email']).id
        user = form.save()
        user.username = f"user-{user.pk}"
        user.save()
        Profile.objects.create(user = user)
        VerificationCode.objects.create(username = user.username, code = special_code)
        send_mail(
            subject = "Код для підтвердження",
            message = f"Вітаємо!\n ваш код для підтвердження: {special_code}",
            from_email = "qrprojectdjangoteam2@gmail.com",
            recipient_list = [f"{form.cleaned_data['email']}"],
            fail_silently = False
            )
        return response

class ConfirmRegistrationView(FormView):
    template_name = "registration_confirm/index.html"
    form_class = VerificationForm
    success_url = reverse_lazy("authorithation")

    def form_valid(self, form):
        input1 = str(form.cleaned_data["input1"])
        input2 = str(form.cleaned_data["input2"])
        input3 = str(form.cleaned_data["input3"])
        input4 = str(form.cleaned_data["input4"])
        input5 = str(form.cleaned_data["input5"])
        input6 = str(form.cleaned_data["input6"])
        
        code_field = input1 + input2 + input3 + input4 + input5 + input6
        email= self.request.COOKIES.get("email")
        username = User.objects.get(email = email).username
        user_code = VerificationCode.objects.get(username = username).code
        
        if user_code == code_field:
            VerificationCode.objects.get(username = username).delete()
            return super().form_valid(form)
        else:
            form.add_error(None, "Код підтвердження не підходе!")
            return self.form_invalid(form)

class AuthorizationView(FormView):
    template_name="authorization/index.html"
    form_class = AuthorithationForm
    success_url = "/"

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(username = email, password = password)
        if user is not None:
            login(self.request, user)

            return super().form_valid(form)
        else:
            form.add_error(None, "Невірна пошта або пароль")
            return self.form_invalid(form)