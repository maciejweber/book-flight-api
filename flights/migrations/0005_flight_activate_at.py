# Generated by Django 3.1.3 on 2021-06-02 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_auto_20210601_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='activate_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Activate at'),
        ),
    ]
