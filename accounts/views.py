from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import render

from .forms import CustomUserLoginForm, CustomSignUpForm, CustomChangeUserForm
from .models import CustomUser

from category.models import category


class SignupView(CreateView):
    form_class = CustomSignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()

        return super().form_valid(form)


class CLoginView(LoginView):
    authentication_form = CustomUserLoginForm
    form_class = CustomUserLoginForm


class ChangeUserView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = CustomChangeUserForm
    template_name = "registration/changeuser.html"
    model = CustomUser
    success_url = reverse_lazy("home")

    def test_func(self):
        return self.get_object() == self.request.user

def settings(request):
    return render(request,"accounts_settings.html",{"user":request.user})