# Generated by Django 4.2.5 on 2023-10-17 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Bookings", "0005_rename_image_bookings_upload_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bookings",
            old_name="upload_image",
            new_name="image",
        ),
    ]