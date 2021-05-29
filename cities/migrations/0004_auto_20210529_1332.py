# Generated by Django 3.1.3 on 2021-05-29 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0003_alter_city_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='display_name',
            field=models.CharField(default='majdan', max_length=30, verbose_name='City name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]