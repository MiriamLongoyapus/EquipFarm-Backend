# Generated by Django 4.2.5 on 2023-09-24 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookings',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='bookings',
            name='equipment_category',
        ),
        migrations.RemoveField(
            model_name='bookings',
            name='equipment_name',
        ),
    ]