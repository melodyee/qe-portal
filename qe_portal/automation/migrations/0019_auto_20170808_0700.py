# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-08 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0018_auto_20170808_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caserunningmodel',
            name='task_id',
            field=models.CharField(blank=True, max_length=48, null=True),
        ),
    ]
