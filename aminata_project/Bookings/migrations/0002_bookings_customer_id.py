# Generated by Django 4.2.5 on 2023-09-15 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='customer_id',
            field=models.CharField(max_length=8, null=True, unique=True),
        ),
    ]
