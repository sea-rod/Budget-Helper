from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import category, category_info


@receiver(post_save, sender=get_user_model())
def create_default_categories(sender, instance, created, **kwargs):
    if created:
        categories = [
            category(user=instance, name="Bills", budget=5000, amt_left=5000),
            category(user=instance, name="Housing", budget=5000, amt_left=5000),
            category(user=instance, name="Transportation", budget=5000, amt_left=5000),
            category(user=instance, name="Groceries", budget=5000, amt_left=5000),
            category(user=instance, name="Entertainment", budget=5000, amt_left=5000),
        ]
        category.objects.bulk_create(categories)


@receiver(post_save, sender=category_info)
def change_amt_left_category(sender, instance, created, **kwargs):
    category_get = category.objects.get(name=instance.cat, user=instance.user)
    category_get.amt_left -= instance.spend
    category_get.save()


@receiver(post_delete, sender=category_info)
def change_amt_left_after_delete(sender, instance, **kwargs):
    category_get = category.objects.get(name=instance.cat, user=instance.user)
    category_get.amt_left += instance.spend
    category_get.save()
