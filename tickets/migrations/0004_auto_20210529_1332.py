# Generated by Django 3.1.3 on 2021-05-29 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_auto_20210529_1332'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0003_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tickets', to='flights.flight', verbose_name='Flight'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tickets', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
