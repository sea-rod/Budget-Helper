from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView,
)

from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.shortcuts import render
from .models import category, category_info
from .form import CatCreateForm, CatInfoForm


class CatInfoListView(ListView):
    template_name = "category_list.html"

    def get_queryset(self):
        return category_info.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        total = category.objects.filter(user=self.request.user).aggregate(
            budget=Coalesce(
                Sum("budget"),
                0.0,
            ),
            amt_left=Coalesce(Sum("amt_left"), 0.00),
        )
        spend = category_info.objects.filter(user=self.request.user).aggregate(
            spend=Coalesce(Sum("spend"), 0.0)
        )

        return super().get_context_data(**kwargs) | total | spend

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        return render(request, "home.html")


class CatCreateView(CreateView):
    model = category
    template_name = "category_add_update.html"
    form_class = CatCreateForm

    def form_valid(self, form):
        budget = form.cleaned_data["budget"]
        if budget <= 0:
            form.add_error("budget", " budget Value must be greater than zero")
            return self.form_invalid(form)

        form.instance.amt_left = budget
        form.instance.user = self.request.user
        return super().form_valid(form)


class CatUpdateView(UpdateView):
    model = category
    template_name = "category_add_update.html"
    form_class = CatCreateForm

    def form_valid(self, form):
        budget = form.cleaned_data["budget"]
        if budget <= 0:
            form.add_error("budget", " budget Value must be greater than zero")
            return self.form_invalid(form)
        form.instance.amt_left = budget
        form.instance.user = self.request.user
        return super().form_valid(form)


class CatDeleteView(DeleteView):
    model = category
    template_name = "category_delete.html"
    success_url = reverse_lazy("home")


class CatViewInfo(DetailView):
    model = category
    template_name = "category_info.html"
    # context_object_name = "category_list"

    # def get_queryset(self):
    #     return category_info.objects.filter(cat=self.kwargs["pk"])

    # def get_context_data(self, **kwargs):
    #     dic = super().get_context_data(**kwargs)

    #     day = category_info.objects.values("date__day", "date__month").annotate(
    #         category_sum=Sum("spend")
    #     )
    #     month = category_info.objects.values("date__month", "date__year").annotate(
    #         category_sum=Sum("spend")
    #     )

    #     cat_wise = category_info.objects.values("cat__name").annotate(
    #         category_sum=Sum("spend")
    #     )
    #     dic["cat_wise"] = cat_wise
    #     dic["month"] = month
    #     dic["day"] = day
    #     return dic


# to add the spendings
class CatInfoAddView(CreateView):
    model = category_info
    form_class = CatInfoForm
    template_name = "category_info_add_update.html"

    def form_valid(self, form):
        spend = form.cleaned_data["spend"]
        cat = form.cleaned_data["cat"]
        if spend <= 0:
            form.add_error("spend", " spend Value must be greater than zero")
            return self.form_invalid(form)

        obj = category.objects.get(name=cat, user=self.request.user)
        obj.amt_left -= spend
        obj.save()

        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


# delete view
class CatInfoDeleteView(DeleteView):
    model = category_info
    template_name = "category_delete.html"
    success_url = reverse_lazy("home")

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.cat.amt_left += obj.spend
        obj.cat.save()

        return super().post(request, *args, **kwargs)
