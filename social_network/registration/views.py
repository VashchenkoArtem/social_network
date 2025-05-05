from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegistrationForm
# Create your views here.


class RegistrationView(FormView):
    template_name = ("registration/index.html")
    form_class = RegistrationForm
    success_url = "registration"
    def form_valid(self, form):
        user = form.save(commit = False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)