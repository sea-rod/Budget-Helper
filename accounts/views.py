from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import CustomUser
from category.models import category
from .forms import CustomUserLoginForm, CustomSignUpForm, CustomChangeUserForm


class SignupView(CreateView):
    form_class = CustomSignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        category.objects.create(user=user, name="Bills", budget=5000, amt_left=5000)
        return super().form_valid(form)


class CLoginView(LoginView):
    authentication_form = CustomUserLoginForm
    form_class = CustomUserLoginForm


class ChangeUserView(UpdateView):
    form_class = CustomChangeUserForm
    template_name = "registration/changeuser.html"
    model = CustomUser
    success_url = reverse_lazy("home")
