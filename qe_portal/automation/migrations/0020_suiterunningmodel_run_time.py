# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-08 07:04
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0019_auto_20170808_0700'),
    ]

    operations = [
        migrations.AddField(
            model_name='suiterunningmodel',
            name='run_time',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]