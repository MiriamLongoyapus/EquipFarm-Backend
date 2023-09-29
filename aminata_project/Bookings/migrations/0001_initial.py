# Generated by Django 4.2.5 on 2023-09-29 16:07

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
                ("customer_name", models.CharField(max_length=32)),
                ("equipment_name", models.CharField(max_length=32)),
                ("equipment_category", models.CharField(max_length=32)),
                ("duration", models.DurationField()),
                ("booking_date", models.DateTimeField()),
            ],
        ),
    ]
