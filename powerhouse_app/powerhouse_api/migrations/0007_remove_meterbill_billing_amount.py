# Generated by Django 3.0.4 on 2020-03-19 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('powerhouse_api', '0006_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meterbill',
            name='billing_amount',
        ),
    ]