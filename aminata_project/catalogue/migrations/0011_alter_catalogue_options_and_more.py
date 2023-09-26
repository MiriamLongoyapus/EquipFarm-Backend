# Generated by Django 4.2.5 on 2023-09-25 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0001_initial"),
        ("catalogue", "0010_alter_catalogue_is_available"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="catalogue",
            options={},
        ),
        migrations.RenameField(
            model_name="catalogue",
            old_name="name",
            new_name="Equipment_name",
        ),
        migrations.AlterField(
            model_name="catalogue",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="category.category",
            ),
        ),
        migrations.DeleteModel(
            name="Category",
        ),
    ]