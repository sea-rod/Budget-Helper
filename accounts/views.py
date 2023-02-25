from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserLoginForm, CustomSignUpForm, CustomChangeUserForm


class SignupView(CreateView):
    form_class = CustomSignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


class CLoginView(LoginView):
    authentication_form = CustomUserLoginForm
    form_class = CustomUserLoginForm


class ChangeUserView(UpdateView):
    form_class = CustomChangeUserForm
    template_name = "registration/changeuser.html"
    model = CustomUser
    success_url = reverse_lazy("home")
