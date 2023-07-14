from django.urls import path
from .views import (
    APIListCreateCategory,
    APIUpdateDeleteRetriveCategory,
    APIListCategoryInfo,
    APIDestoryCategoryInfo,
)

urlpatterns = [
    path("", APIListCreateCategory.as_view()),
    path("<int:pk>/category/", APIUpdateDeleteRetriveCategory.as_view()),
    path("<int:pk>/delete_catinfo/", APIDestoryCategoryInfo.as_view()),
    path("list_category/", APIListCategoryInfo.as_view()),
]
