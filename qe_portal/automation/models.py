# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django import utils
from django.core.validators import MaxValueValidator, MinValueValidator
from simple_history.models import HistoricalRecords

from markdownx.models import MarkdownxField

import datetime

# Create your models here.


class CaseModel(models.Model):
    TYPE_CHOICES = (
        ('web', 'TC_WEB'),
        ('ios', 'TC_IOS'),
        ('android', 'TC_ANDROID'),
        ('es', 'TC_EMBEDDED'),
        ('vision', 'TC_VISION'),
        ('fc', 'TC_FC'),
    )

    PLATFORM_CHOICES = (
        ('win', 'WIN'),
        ('mac', 'MAC'),
        ('linux', 'LNX'),
    )

    type = models.CharField(max_length=16, null=False, choices=TYPE_CHOICES)
    name = models.CharField(max_length=128, null=False)
    description = models.TextField(default="", max_length=512, null=True, blank=True)
    cmd = models.CharField(max_length=32)
    params = models.CharField(max_length=128, null=True, blank=True)
    script = models.CharField(max_length=256)
    platform = models.CharField(max_length=32, choices=PLATFORM_CHOICES )
    timeout = models.IntegerField(default=120)

    history = HistoricalRecords()

    def __unicode__(self):
        return self.name + " : " + self.type + " : " + self.description


class SuiteModel(models.Model):
    name = models.CharField(default="", max_length=128, null=False, blank=False)
    description = models.TextField(default="", max_length=512, null=True, blank=True)
    create_time = datetime.datetime.now()
    emails = models.CharField(max_length=256, null=True, blank=True)
    cases = models.ManyToManyField(CaseModel)

    history = HistoricalRecords()

    def __unicode__(self):
        return unicode(self.name + self.description) or u''


class SchedulerModel(models.Model):
    name = models.CharField(max_length=128, null=False)
    description = models.TextField(default="", max_length=512, null=True, blank=True)
    suite = models.ForeignKey(SuiteModel)
    SCHED_TYPE = (
        ('ManualRun', 'Run Manually!'),
        ('RepeatEveryDay', 'Every Day!'),
        ('RepeatWorkingDay', 'Every WorkingDay!'),
        ('Reserved', 'Reserved'),
    )
    type = models.CharField(max_length=16, choices=SCHED_TYPE,)
    create_time = models.DateTimeField(default=utils.timezone.now, null=True, blank=True)
    # create_time = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True)
    emails = models.CharField(max_length=256, null=True, blank=True)
    appoint_at = models.TimeField(default=utils.timezone.now, null=True, blank=True)
    start_day = models.DateField(default=utils.timezone.now, null=True, blank=True)
    end_day = models.DateField(default=utils.timezone.now, null=True, blank=True)
    # appoint_at = models.TimeField(default=datetime.datetime.now(), null=True, blank=True)
    # start_day = models.DateField(default=datetime.datetime.now(), null=True, blank=True)
    # end_day = models.DateField(default=datetime.datetime.now(), null=True, blank=True)
    status = models.BooleanField(default=True)

    history = HistoricalRecords()

    def __unicode__(self):
        return self.name + ":" + self.type + ":" + self.description


class CaseRunningModel(models.Model):
    case = models.ForeignKey(CaseModel)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    run_time = models.IntegerField(default=0, validators=[MinValueValidator(0),], null=True, blank=True)
    ret_code = models.IntegerField(default=1, )
    error_msg = models.CharField(max_length=128, null=True, blank=True)
    log = models.CharField(max_length=128, null=True, blank=True)
    task_id = models.CharField(max_length=48, null=True, blank=True)

    def __unicode__(self):
        return "CaseRun:%s:%s:%s" % (self.pk, self.case.name, self.start_time)


class SuiteRunningModel(models.Model):
    suite = models.ForeignKey(SuiteModel)
    schedule = models.ForeignKey(SchedulerModel, default=5)
    case_runnings = models.ManyToManyField(CaseRunningModel)

    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    run_time = models.IntegerField(default=0, validators=[MinValueValidator(0),], null=True, blank=True)
    ret = models.IntegerField(default=1, blank=True, null=True)
    error_msg = models.CharField(max_length=256, null=True, blank=True)
    STATUS_TYPE = (
        ('Pending', 'Pending'),
        ('Running', 'Running'),
        ('Scheduled', 'Scheduled'),
        ('Completed','Completed'),
    )
    status = models.CharField(max_length=16, choices=STATUS_TYPE, default='Pending')
    progress = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])

    def __unicode__(self):
        return "SuiteRun:" + self.pk + ":" + self.suite.name + ":" + self.start_time


class RequirementModel(models.Model):
    Requirement = MarkdownxField()




