# Generated by Django 4.2.5 on 2023-10-20 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("register", "0001_initial"),
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=1, null=True)),
                ("is_added", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "purchase_option",
                    models.CharField(
                        choices=[
                            ("buy", "Buy"),
                            ("rent", "Rent"),
                            ("hire_purchase", "Hire Purchase"),
                        ],
                        default="buy",
                        max_length=20,
                    ),
                ),
                (
                    "catalogue",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="category.catalogue",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="register.farmer",
                    ),
                ),
            ],
        ),
    ]
