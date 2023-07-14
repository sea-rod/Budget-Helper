from rest_framework import serializers
from category.models import category, category_info


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "budget")
        model = category


class CategoryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "spend", "cat", "item", "date")
        model = category_info
