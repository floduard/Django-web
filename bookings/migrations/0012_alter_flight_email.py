# Generated by Django 4.2.4 on 2023-08-27 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0011_alter_flight_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
