# Generated by Django 5.1.1 on 2024-12-25 03:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pharmacy', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacy',
            name='employees',
            field=models.ManyToManyField(blank=True, limit_choices_to={'is_staff': True}, to=settings.AUTH_USER_MODEL, verbose_name='Сотрудники'),
        ),
    ]
