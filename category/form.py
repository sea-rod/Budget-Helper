from django import forms
from .models import category


class CatCreateForm(forms.ModelForm):
    name = forms.CharField(
        label="Category Name",
        widget=forms.TextInput(
            attrs={
                "class": "some_class",
            }
        ),
    )

    budget = forms.FloatField(
        label="Budget for this month",
        widget=forms.NumberInput(
            attrs={
                "class": "some_class",
            }
        ),
    )

    class Meta:
        model = category
        fields = ("name", "budget")
