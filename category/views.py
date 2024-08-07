from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView,
    TemplateView,
)
from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .form import CatCreateForm, CatInfoForm
from .models import category, category_info
from .services import amt_remaining, get_budget_summary


class CatListView(LoginRequiredMixin, ListView):
    model = category
    template_name = "category_list.html"

    def get_queryset(self):
        return category.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        budget_summary = get_budget_summary(user=self.request.user)

        return super().get_context_data(**kwargs) | budget_summary


class CatCreateView(LoginRequiredMixin, CreateView):
    model = category
    template_name = "category_add.html"
    form_class = CatCreateForm

    def form_valid(self, form):
        budget = form.cleaned_data["budget"]
        form.instance.amt_left = budget
        form.instance.user = self.request.user
        return super().form_valid(form)


class CatUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = category
    template_name = "category_update.html"
    form_class = CatCreateForm

    def form_valid(self, form):
        budget = form.cleaned_data["budget"]
        form.instance.amt_left = amt_remaining(form.instance.user, budget)
        form.instance.user = self.request.user
        form.instance.budget = budget
        return super().form_valid(form)

    def test_func(self):
        return self.get_object().user == self.request.user


class CatDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = category
    template_name = "category_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        return self.get_object().user == self.request.user


class CatViewInfo(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = category
    template_name = "category_detail.html"
    query = None

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        search = request.GET.get("search")
        if search:
            query_list = search.split(":")
            if len(query_list) > 1:
                self.query = ...
            # context = self.get_context_data()
            self.query = self.get_object().cat_info.filter(
                item__icontains=request.GET["search"]
            )
        return super().get(request, *args, **kwargs)

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sum_per_day"] = (
            context["category"]
            .cat_info.extra(select={"day": "date( date )"})
            .values("day")
            .annotate(day_sum=Sum("spend"))[:15]
        )
        p = self.request.GET.get("page")
        if self.query is not None:
            context["page_obj"] = Paginator(self.query,2).get_page(p)
            context["search"] = True
            return context
        context["page_obj"] = Paginator(context["category"].cat_info.all(), 5).get_page(
            p
        )

        return context


class CatInfoListView(ListView):
    template_name = "category_info_list.html"

    def get_queryset(self):
        return category_info.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        budget_summary = get_budget_summary(user=self.request.user)

        return super().get_context_data(**kwargs) | budget_summary

    def get(self, request, *args, **kwargs):
        print(request.user.is_authenticated)
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        return render(request, "home.html")


# to add the spendings
class CatInfoAddView(LoginRequiredMixin, CreateView):
    model = category_info
    form_class = CatInfoForm
    template_name = "category_info_add_update.html"

    def form_valid(self, form):
        form.instance.item = form.instance.item.title()
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


# delete view
class CatInfoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = category_info
    template_name = "category_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        return self.get_object().user == self.request.user


class Settings(TemplateView):
    template_name = "settings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = category.objects.filter(user_id=self.request.user)
        context["category"] = data
        return context
