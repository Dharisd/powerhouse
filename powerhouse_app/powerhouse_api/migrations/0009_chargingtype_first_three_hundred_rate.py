# Generated by Django 3.0.4 on 2020-03-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerhouse_api', '0008_meterbill_bill_chargingtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='chargingtype',
            name='first_three_hundred_rate',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
    ]
