# Generated by Django 3.0.4 on 2020-03-19 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('powerhouse_api', '0005_auto_20200319_0430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_type', models.CharField(choices=[('ONLINE', 'ONLINE'), ('CASH', 'CASH')], default='ONLINE', max_length=6)),
                ('payment_identifier', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('payment_datetime', models.DateTimeField()),
                ('payment_creation_method', models.CharField(choices=[('AUTOGEN', 'AUTOGEN'), ('MANUAL', 'MANUAL')], default='AUTOGEN', max_length=8)),
                ('payment_bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='powerhouse_api.MeterBill')),
                ('payment_created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
