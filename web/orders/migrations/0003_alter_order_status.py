# Generated by Django 3.2.5 on 2022-10-12 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('unpaid', 'Unpaid'), ('payment_fail', 'Payment Fail'), ('waiting_for_shipment', 'Waiting for shipment'), ('transporting', 'Transporting'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='unpaid', max_length=100, verbose_name='Status'),
        ),
    ]
