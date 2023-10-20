# Generated by Django 4.2.5 on 2023-10-20 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Bookings", "0002_bookings_date_returned_bookings_image"),
        ("register", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookings",
            name="phone_number",
            field=models.OneToOneField(
                default=2344567,
                on_delete=django.db.models.deletion.CASCADE,
                to="register.customuser",
            ),
            preserve_default=False,
        ),
    ]
