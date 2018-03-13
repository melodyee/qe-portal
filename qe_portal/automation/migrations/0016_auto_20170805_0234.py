# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-05 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0015_auto_20170804_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suiterunningmodel',
            name='ret',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='suiterunningmodel',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Running', 'Running'), ('Scheduled', 'Scheduled'), ('Completed', 'Completed')], default='Pending', max_length=16),
        ),
    ]
