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


class BudgetSummarySerializer(serializers.Serializer):
    budget = serializers.FloatField()
    amt_left = serializers.FloatField()
    spend = serializers.FloatField()
