# Generated by Django 4.2.4 on 2023-08-22 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_delete_bus_delete_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
