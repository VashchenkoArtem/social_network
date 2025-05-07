from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import RegistrationForm


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = "registration/index.html"
    success_url = reverse_lazy("registration")
# from .forms import RegistrationForm
# # Create your views here.


# class RegistrationView(FormView):
#     template_name = ("registration/index.html")
#     form_class = RegistrationForm
#     success_url = "registration"
#     def form_valid(self, form):
#         user = form.save(commit = False)
#         user.set_password(form.cleaned_data['password'])
#         user.save()
#         return super().form_valid(form)