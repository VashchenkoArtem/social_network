from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from .forms import RegistrationForm
from .forms import VerificationForm
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView
import random
from django.contrib.auth.models import User
from .models import SpecialCode



class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = "registration/index.html"
    success_url = reverse_lazy("confirm")

    def form_valid(self, form):
        response = super().form_valid(form)
        response.set_cookie('username', form.cleaned_data['username'], max_age=3600)
        special_code = random.randint(0, 999999)
        user_id = User.objects.get(username = form.cleaned_data['username']).id
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
        username= self.request.COOKIES.get("username")
        user_id = User.objects.get(username = username).id
        user_code = SpecialCode.objects.get(user_id = user_id).verification_code
        if user_code == code_field:
            return super().form_valid(form)
        else:
            form.add_error("verification_code", "Код підтвердження не підходе!")
            return self.form_invalid(form)

class AuthorizationView(LoginView):
    template_name="authorization/index.html"