from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.db.models import Model
from .models import category_info, category


def amt_remaining(user: Model, budget: int) -> int:
    """
    Calculates the remaining amount after deducting the spend from the budget.

    Args:
        user (Model): Instance of the user model.
        budget (int): Budget of the user.

    Returns:
        int: The remaining amount after deducting the spend from the budget.
    """
    spend = category_info.objects.filter(user=user).aggregate(
        spend=Coalesce(Sum("spend"), 0.0)
    )["spend"]
    return budget - spend


def get_budget_summary(user: Model) -> dict:
    """
    Returns the budget summary i.e amount left,spent and total budget

    Args:
        user (Model): Instance of the user model.

    Returns:
        dict: Summary of the budget i.e amount left,spent and total budget
    """
    total = category.objects.filter(user=user).aggregate(
        budget=Coalesce(
            Sum("budget"),
            0.0,
        ),
        amt_left=Coalesce(Sum("amt_left"), 0.00),
    )
    spent = category_info.objects.filter(user=user).aggregate(
        spend=Coalesce(Sum("spend"), 0.0)
    )

    return total | spent
