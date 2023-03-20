from django.urls import path
from .views import (
    CatInfoListView,
    CatInfoDeleteView,
    CatViewInfo,
    CatListView,
    CatCreateView,
    CatUpdateView,
    CatDeleteView,
    CatInfoAddView,
)

urlpatterns = [
    path("", CatInfoListView.as_view(), name="home"),
    path("info/add/", CatInfoAddView.as_view(), name="cat_info_add"),
    path("info/<int:pk>/delete/", CatInfoDeleteView.as_view(), name="cat_info_delete"),
    path("category_add/", CatCreateView.as_view(), name="cat_add"),
    path("settings/category", CatListView.as_view(), name="cat_list"),
    path("<int:pk>/category_info/", CatViewInfo.as_view(), name="info"),
    path("<int:pk>/category_update/", CatUpdateView.as_view(), name="cat_update"),
    path("<int:pk>/category_delete/", CatDeleteView.as_view(), name="cat_delete"),
]
