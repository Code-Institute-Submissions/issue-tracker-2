# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-09 16:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0015_auto_20180909_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featureticket',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
