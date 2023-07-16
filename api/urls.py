from django.urls import path
from .views import (
    APIListCreateCategory,
    APIUpdateDeleteRetriveCategory,
    APIListCategoryInfo,
    APIDestoryCategoryInfo,
    BudgetSummary,
)

urlpatterns = [
    path("", APIListCreateCategory.as_view()),
    path("<int:pk>/category/", APIUpdateDeleteRetriveCategory.as_view()),
    path("<int:pk>/delete_catinfo/", APIDestoryCategoryInfo.as_view()),
    path("list_category/", APIListCategoryInfo.as_view()),
    path("get_summary/", BudgetSummary.as_view()),
]
