# Generated by Django 4.2.5 on 2023-09-25 00:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0006_rename_date_payment_data_work"),
    ]

    operations = [
        migrations.RenameField(
            model_name="payment",
            old_name="data_work",
            new_name="data",
        ),
    ]