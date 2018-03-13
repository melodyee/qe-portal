# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-10 07:52
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('automation', '0047_auto_20170810_0752'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalSchedulerModel',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, default='', max_length=512, null=True)),
                ('type', models.CharField(choices=[('ManualRun', 'Run Manually!'), ('RepeatEveryDay', 'Every Day!'), ('RepeatWorkingDay', 'Every WorkingDay!'), ('Reserved', 'Reserved')], max_length=16)),
                ('create_time', models.DateTimeField(blank=True, default=datetime.datetime(2017, 8, 10, 7, 52, 59, 266584), null=True)),
                ('emails', models.CharField(blank=True, max_length=256, null=True)),
                ('appoint_at', models.TimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('start_day', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('end_day', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('suite', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='automation.SuiteModel')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical scheduler model',
            },
        ),
        migrations.AlterField(
            model_name='schedulermodel',
            name='appoint_at',
            field=models.TimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='schedulermodel',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 8, 10, 7, 52, 59, 266584), null=True),
        ),
        migrations.AlterField(
            model_name='schedulermodel',
            name='end_day',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='schedulermodel',
            name='start_day',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
