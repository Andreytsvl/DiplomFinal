# Generated by Django 5.1.1 on 2024-12-26 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_pharmacy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='requires_delivery',
        ),
    ]
