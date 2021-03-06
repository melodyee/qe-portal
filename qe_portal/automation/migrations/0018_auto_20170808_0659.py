# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-08 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0017_auto_20170805_0740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suitemodel',
            name='scheduler',
        ),
        migrations.AddField(
            model_name='caserunningmodel',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='caserunningmodel',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='suitemodel',
            name='description',
            field=models.TextField(blank=True, max_length=512, null=True),
        ),
    ]
