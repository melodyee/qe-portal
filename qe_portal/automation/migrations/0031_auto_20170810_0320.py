# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-10 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0030_auto_20170810_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalschedulermodel',
            name='description',
            field=models.TextField(blank=True, default='', max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='schedulermodel',
            name='description',
            field=models.TextField(blank=True, default='', max_length=512, null=True),
        ),
    ]