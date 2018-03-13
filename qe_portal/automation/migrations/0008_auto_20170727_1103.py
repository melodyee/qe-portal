# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 11:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0007_schedulermodel_schedulerrunningmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulerrunningmodel',
            name='progress',
            field=models.IntegerField(default=0, max_length=3, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='schedulermodel',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='schedulerrunningmodel',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Running', 'Running'), ('Completed', 'Completed')], default='Pending', max_length=16),
        ),
    ]