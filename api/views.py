from rest_framework import generics, permissions
from category.models import category, category_info
from category.services import get_budget_summary
from rest_framework.response import Response
from .permissions import UserOnly
from .serializer import (
    CategorySerializer,
    CategoryInfoSerializer,
    BudgetSummarySerializer,
)


class APIListCreateCategory(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user, amt_left=serializer.validated_data.get("budget")
        )


class APIUpdateDeleteRetriveCategory(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated, UserOnly)

    def get_queryset(self):
        return category.objects.filter(user=self.request.user)


class APIListCategoryInfo(generics.ListAPIView):
    serializer_class = CategoryInfoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        cat = self.request.query_params.get("category", None)
        if cat:
            return category_info.objects.filter(user=user, cat=cat)
        return category_info.objects.filter(user=user)


class APIDestoryCategoryInfo(generics.DestroyAPIView):
    serializer_class = CategoryInfoSerializer
    permission_classes = (permissions.IsAuthenticated, UserOnly)

    def get_queryset(self):
        return category.objects.filter(user=self.request.user)


class BudgetSummary(generics.GenericAPIView):
    serializer_class = BudgetSummarySerializer
    permission_classes = (permissions.IsAuthenticated, UserOnly)

    def get(self, request, *args, **kwargs):
        user = request.user
        budget_summary = get_budget_summary(user)
        serializer_data = self.get_serializer(budget_summary)

        return Response(serializer_data.data)
