# Generated by Django 3.0.4 on 2020-03-20 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('powerhouse_api', '0007_remove_meterbill_billing_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='meterbill',
            name='bill_chargingtype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='powerhouse_api.ChargingType'),
        ),
    ]
