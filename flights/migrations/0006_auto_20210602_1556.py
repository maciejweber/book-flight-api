# Generated by Django 3.1.3 on 2021-06-02 13:56

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_flight_activate_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='first_class_ticket_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='First class ticket price'),
        ),
    ]
