# Generated by Django 4.2.5 on 2023-09-18 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_rename_payment_date_payment_payment_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
    ]
