from django.apps import AppConfig


class CategoryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "category"

    def ready(self) -> None:
        from .signals import (
            create_default_categories,
            change_amt_left_after_delete,
            change_amt_left_category,
        )
