# Generated by Django 4.2.5 on 2023-10-19 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Bookings", "0006_rename_upload_image_bookings_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookings",
            name="date_returned",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
