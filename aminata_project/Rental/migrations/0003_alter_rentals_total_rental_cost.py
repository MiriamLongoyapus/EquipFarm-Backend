# Generated by Django 4.2.5 on 2023-09-22 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rental', '0002_remove_rentals_payment_option_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentals',
            name='total_rental_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
        model_name='Rentals',
        name='rental_period',
        field=models.DurationField(),  
        ),
    ]


