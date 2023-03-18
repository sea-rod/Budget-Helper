from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model


class category(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    budget = models.FloatField(default=0)
    amt_left = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("home")


class category_info(models.Model):
    cat = models.ForeignKey(category, on_delete=models.CASCADE)
    spend = models.FloatField()
    item = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.cat}_info {self.date.ctime()}"

    def get_absolute_url(self):
        return reverse_lazy("home")
