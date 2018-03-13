# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-08 11:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0027_auto_20170808_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedulermodel',
            name='repeat_at',
        ),
        migrations.AlterField(
            model_name='schedulermodel',
            name='appoint_at',
            field=models.TimeField(blank=True, default=datetime.datetime(2017, 8, 8, 11, 17, 7, 447886), null=True),
        ),
        migrations.AlterField(
            model_name='schedulermodel',
            name='end_day',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 8, 8, 11, 17, 7, 447965), null=True),
        ),
        migrations.AlterField(
            model_name='schedulermodel',
            name='start_day',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 8, 8, 11, 17, 7, 447932), null=True),
        ),
    ]