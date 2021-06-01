# Generated by Django 3.1.3 on 2021-05-31 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='City name')),
                ('display_name', models.CharField(help_text='Display name should stary with a capital letter', max_length=30, unique=True, verbose_name='Display name')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='countries.country')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
    ]
