# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-08 08:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0024_auto_20170808_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulermodel',
            name='end_time',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 8, 8, 8, 8, 9, 486862), null=True),
        ),
        migrations.AlterField(
            model_name='schedulermodel',
            name='start_time',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 8, 8, 8, 8, 9, 486839), null=True),
        ),
    ]
