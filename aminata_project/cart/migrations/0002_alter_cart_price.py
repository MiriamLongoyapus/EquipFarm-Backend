# Generated by Django 4.2.5 on 2023-09-30 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
