# Generated by Django 4.2.5 on 2023-09-22 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0007_alter_catalogue_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="catalogue",
            name="price",
            field=models.IntegerField(),
        ),
    ]