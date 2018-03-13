# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from automation.models import CaseModel
from automation.models import SuiteModel
from automation.models import SchedulerModel

from automation.models import CaseRunningModel
from automation.models import SuiteRunningModel

# Register your models here.

class CaseModelAdmin(admin.ModelAdmin):
    pass

class SuiteModelAdmin(admin.ModelAdmin):
    pass

class SchedulerModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(CaseModel, CaseModelAdmin)
admin.site.register(SuiteModel, SuiteModelAdmin)
admin.site.register(SchedulerModel, SchedulerModelAdmin)

class CaseRunningModelAdmin(admin.ModelAdmin):
    pass

class SuiteRunningModelAdmin(admin.ModelAdmin):
    pass

class SchedulerModelAdmin(admin.ModelAdmin):
    pass

# admin.site.register(CaseRunningModel, CaseRunningModelAdmin)
# admin.site.register(SuiteRunningModel, SuiteRunningModelAdmin)

