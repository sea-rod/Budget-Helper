from rest_framework import generics, permissions
from category.models import category, category_info
from .permissions import UserOnly
from .serializer import CategorySerializer, CategoryInfoSerializer


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
