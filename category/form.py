from django import forms
from .models import category, category_info


class CatCreateForm(forms.ModelForm):
    name = forms.CharField(
        label="Category Name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control cat-fields",
                "placeholder": "e.g Bills",
            }
        ),
    )

    budget = forms.FloatField(
        label="Budget for this month",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control cat-fields",
                "placeholder": "e.g 1000",
            }
        ),
    )

    class Meta:
        model = category
        fields = ("name", "budget")


class CatInfoForm(forms.ModelForm):
    user = None
    cat = forms.ModelChoiceField(
        label="Category",
        queryset=category.objects.filter(user=user),
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
                "placeholder": "e.g 1000",
            }
        ),
    )
    item = forms.CharField(
        label="item",
        widget=forms.TextInput(
            attrs={
                "class": "form-control cat-fields",
                "placeholder": "e.g Electricity bill",
            }
        ),
    )

    class Meta:
        model = category_info
        fields = ("cat", "spend", "item")

    def __init__(self, *args, **kwargs):
        user = kwargs["user"]
        del kwargs["user"]
        super(CatInfoForm, self).__init__(*args, **kwargs)
        self.fields["cat"].queryset = category.objects.filter(user=user)
