# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-07 10:33
from __future__ import unicode_literals

from django.db import migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_ticket_status_changed'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='feature_status',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default='to do', max_length=100, no_check_for_status=True, verbose_name='bug'),
        ),
    ]
