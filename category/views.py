from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.db.models import Sum
from django.db.models.functions import ExtractMonth
from .models import category, category_info
from .form import CatCreateForm


class CatView(ListView):
    template_name = "category_list.html"

    def get_queryset(self):
        return category.objects.filter(user=self.request.user)


class CatCreateView(CreateView):
    model = category
    template_name = "category_add_update.html"
    form_class = CatCreateForm

    def form_valid(self, form):
        budget = form.cleaned_data["budget"]
        if budget <= 0:
            form.add_error("budget", " budget Value must be greater than zero")
            return self.form_invalid(form)

        form.instance.user = self.request.user
        return super().form_valid(form)


class CatUpdateView(UpdateView):
    model = category
    template_name = "category_add_update.html"
    form_class = CatCreateForm


class CatDeleteView(DeleteView):
    model = category
    template_name = "category_delete.html"
    success_url = reverse_lazy("home")


class CatViewInfo(ListView):
    template_name = "category_info.html"
    context_object_name = "category_info_list"

    def get_queryset(self):
        return category_info.objects.filter(cat=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        dic = super().get_context_data(**kwargs)

        day = category_info.objects.values("date__day", "date__month").annotate(
            category_sum=Sum("spend")
        )
        month = category_info.objects.values("date__month", "date__year").annotate(
            category_sum=Sum("spend")
        )

        cat_wise = category_info.objects.values("cat__name").annotate(
            category_sum=Sum("spend")
        )
        dic["cat_wise"] = cat_wise
        dic["month"] = month
        dic["day"] = day
        return dic


class CatInfoAddView(CreateView):
    model = category_info
    fields = ("cat", "spend", "item")
