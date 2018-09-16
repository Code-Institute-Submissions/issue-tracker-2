# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-15 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0020_auto_20180915_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='updated_date',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
