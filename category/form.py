from django import forms
from .models import category, category_info


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


class CatInfoForm(forms.ModelForm):
    cat = forms.ModelChoiceField(
        label="Category",
        queryset=category.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control cat-fields",
            }
        ),
    )
    spend = forms.IntegerField(
        label="spent",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control cat-fields",
            }
        ),
    )
    item = forms.CharField(
        label="item",
        widget=forms.TextInput(
            attrs={
                "class": "form-control cat-fields",
            }
        ),
    )

    class Meta:
        model = category_info
        fields = ("cat", "spend", "item")
