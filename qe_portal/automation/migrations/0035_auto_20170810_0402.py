# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-10 04:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0034_auto_20170810_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalschedulermodel',
            name='appoint_at',
            field=models.TimeField(blank=True, default=datetime.datetime(2017, 8, 10, 4, 2, 52, 67193), null=True),
        ),
        migrations.AlterField(
            model_name='historicalschedulermodel',
            name='end_day',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 8, 10, 4, 2, 52, 67246), null=True),
        ),
        migrations.AlterField(
            model_name='historicalschedulermodel',
            name='start_day',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 8, 10, 4, 2, 52, 67222), null=True),
        ),
        migrations.AlterField(
            model_name='schedulermodel',
            name='appoint_at',
            field=models.TimeField(blank=True, default=datetime.datetime(2017, 8, 10, 4, 2, 52, 67193), null=True),
        ),
        migrations.AlterField(
            model_name='schedulermodel',
            name='end_day',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 8, 10, 4, 2, 52, 67246), null=True),
        ),
        migrations.AlterField(
            model_name='schedulermodel',
            name='start_day',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 8, 10, 4, 2, 52, 67222), null=True),
        ),
    ]
