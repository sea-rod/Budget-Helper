from django.urls import path
from .views import (
    CatView,
    CatViewInfo,
    CatCreateView,
    CatUpdateView,
    CatDeleteView,
    CatInfoAddView,
)

urlpatterns = [
    path("", CatView.as_view(), name="home"),
    path("<int:pk>/info/", CatViewInfo.as_view(), name="info"),
    path("category_add/", CatCreateView.as_view(), name="cat_add"),
    path("<int:pk>/category_update/", CatUpdateView.as_view(), name="cat_update"),
    path("<int:pk>/category_delete/", CatDeleteView.as_view(), name="cat_delete"),
    path("info/add/", CatInfoAddView.as_view(), name="cat_info_add"),
]
