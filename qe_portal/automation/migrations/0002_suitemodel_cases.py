# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-22 02:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='suitemodel',
            name='cases',
            field=models.ManyToManyField(blank=True, to='automation.TC_Model'),
        ),
    ]
