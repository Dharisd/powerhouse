# Generated by Django 3.0.4 on 2020-09-14 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('powerhouse_api', '0012_auto_20200506_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meterreading',
            name='reading_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
