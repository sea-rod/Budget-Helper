from django.contrib.auth import password_validation
from .models import CustomUser
from django.contrib.auth.forms import (
    AuthenticationForm,
    UsernameField,
    UserCreationForm,
    UserChangeForm,
)
from django.utils.translation import gettext_lazy as _
from django import forms


class CustomUserLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "placeholder": "Username",
                "class": "form-control fields",
            }
        )
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "placeholder": "Password",
                "class": "form-control fields",
            }
        ),
    )


class CustomSignUpForm(UserCreationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "placeholder": "Username",
                "class": "form-control fields",
            }
        )
    )
    email = forms.EmailField(
        label=_("Email"),
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control fields",
            }
        ),
    )
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "form-control fields",
                "placeholder": "password",
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "form-control fields",
                "placeholder": "password",
            }
        ),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email")


class CustomChangeUserForm(UserChangeForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "placeholder": "Username",
                "class": "form-control fields",
            }
        )
    )
    email = forms.EmailField(
        label=_("Email"),
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control fields",
            }
        ),
    )
    profile_pic = forms.ImageField(
        label=("Add profile_pic"),
        widget=forms.FileInput(
            attrs={
                "placeholder": "File",
                "class": "form-control fields",
                "accept": "image/*",
            }
        ),
    )

    class Meta:
        model = CustomUser
        fields = ("profile_pic", "username", "email")
        field_classes = {"username": UsernameField}
