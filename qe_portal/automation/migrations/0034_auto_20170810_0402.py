# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-10 04:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0033_auto_20170810_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalschedulermodel',
            name='appoint_at',
            field=models.TimeField(blank=True, default=datetime.datetime(2017, 8, 10, 4, 2, 44, 609251), null=True),
        ),
        migrations.AlterField(
            model_name='historicalschedulermodel',
            name='end_day',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 8, 10, 4, 2, 44, 609321), null=True),
        ),
        migrations.AlterField(
            model_name='historicalschedulermodel',
            name='start_day',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 8, 10, 4, 2, 44, 609301), null=True),
        ),
        migrations.AlterField(
            model_name='historicalschedulermodel',
            name='type',
            field=models.CharField(choices=[('ManualRun', 'Run Manually!'), ('RepeatEveryDay', 'Every Day!'), ('RepeatWorkingDay', 'Every WorkingDay!'), ('Reserved', 'Reserved')], max_length=16),
        ),
        migrations.AlterField(
            model_name='schedulermodel',
            name='appoint_at',
            field=models.TimeField(blank=True, default=datetime.datetime(2017, 8, 10, 4, 2, 44, 609251), null=True),
        ),
        migrations.AlterField(
            model_name='schedulermodel',
            name='end_day',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 8, 10, 4, 2, 44, 609321), null=True),
        ),
        migrations.AlterField(
            model_name='schedulermodel',
            name='start_day',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 8, 10, 4, 2, 44, 609301), null=True),
        ),
        migrations.AlterField(
            model_name='schedulermodel',
            name='type',
            field=models.CharField(choices=[('ManualRun', 'Run Manually!'), ('RepeatEveryDay', 'Every Day!'), ('RepeatWorkingDay', 'Every WorkingDay!'), ('Reserved', 'Reserved')], max_length=16),
        ),
    ]
