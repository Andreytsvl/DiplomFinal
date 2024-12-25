# Generated by Django 5.1.1 on 2024-12-25 05:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_initial'),
        ('pharmacy', '0003_pharmacy_facade_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pharmacy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacy.pharmacy', verbose_name='Аптека для самовывоза'),
        ),
    ]
