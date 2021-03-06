# Generated by Django 3.0.4 on 2020-05-06 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerhouse_api', '0011_payment_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_status',
            field=models.CharField(choices=[('APPROVED', 'APPROVED'), ('PENDING', 'PENDING'), ('REJECTED', 'REJECTED')], default='PENDING', max_length=8),
        ),
    ]
