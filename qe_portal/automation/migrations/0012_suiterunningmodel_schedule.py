# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-03 04:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0011_auto_20170803_0346'),
    ]

    operations = [
        migrations.AddField(
            model_name='suiterunningmodel',
            name='schedule',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='automation.SchedulerModel'),
        ),
    ]