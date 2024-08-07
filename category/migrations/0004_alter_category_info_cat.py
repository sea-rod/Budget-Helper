# Generated by Django 4.1.7 on 2024-07-31 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("category", "0003_alter_category_info_cat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category_info",
            name="cat",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cat_info",
                to="category.category",
            ),
        ),
    ]
