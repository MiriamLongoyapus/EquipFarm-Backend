# Generated by Django 4.2.5 on 2023-09-26 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0014_alter_catalogue_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="catalogue",
            old_name="name",
            new_name="equipment_name",
        ),
    ]