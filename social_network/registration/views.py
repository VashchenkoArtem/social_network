from django.views.generic.edit import CreateView, FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import RegistrationForm
from .forms import VerificationForm, AuthorithationForm
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView
import random
from django.contrib.auth.models import User
from .models import SpecialCode
from django.contrib.auth import authenticate, login


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = "registration/index.html"
    success_url = reverse_lazy("confirm")

    def form_valid(self, form):
        response = super().form_valid(form)
        response.set_cookie('email', form.cleaned_data['email'], max_age=3600)
        special_code = random.randint(99999, 999999)
        user_id = User.objects.get(email = form.cleaned_data['email']).id
        SpecialCode.objects.create(verification_code = special_code, user_id = user_id)
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
        code_field = form.cleaned_data['verification_code']
        email= self.request.COOKIES.get("email")
        user_id = User.objects.get(email = email).id
        user_code = SpecialCode.objects.get(user_id = user_id).verification_code
        if user_code == code_field:
            return super().form_valid(form)
        else:
            form.add_error("verification_code", "Код підтвердження не підходе!")
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