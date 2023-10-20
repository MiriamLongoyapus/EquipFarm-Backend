# Generated by Django 4.2.5 on 2023-10-04 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bookings",
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
                ("duration", models.DurationField()),
                ("customer_name", models.CharField(default="Customer", max_length=255)),
                (
                    "equipment_name",
                    models.CharField(default="Default Equipment", max_length=32),
                ),
                (
                    "equipment_category",
                    models.CharField(default="Default Category", max_length=32),
                ),
                ("booking_date", models.DateTimeField()),
            ],
        ),
    ]
