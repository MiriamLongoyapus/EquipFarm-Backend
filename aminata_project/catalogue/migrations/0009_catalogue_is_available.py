# Generated by Django 4.2.5 on 2023-09-22 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0008_alter_catalogue_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="catalogue",
            name="is_available",
            field=models.BooleanField(default=True),
        ),
    ]