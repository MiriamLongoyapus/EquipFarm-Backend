# Generated by Django 4.2.5 on 2023-09-13 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0002_alter_catalogue_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="catalogue",
            options={"verbose_name_plural": "catalog"},
        ),
        migrations.AlterField(
            model_name="catalogue",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
