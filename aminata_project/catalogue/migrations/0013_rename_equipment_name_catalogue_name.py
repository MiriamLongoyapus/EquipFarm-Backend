# Generated by Django 4.2.5 on 2023-09-26 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0012_rename_equipment_name_catalogue_equipment_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="catalogue",
            old_name="equipment_name",
            new_name="name",
        ),
    ]