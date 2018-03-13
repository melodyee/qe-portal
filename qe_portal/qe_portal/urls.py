"""qe_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.views.i18n import JavaScriptCatalog

from automation.views import Dashboard

from automation.views import CaseNew
from automation.views import CaseEdit
from automation.views import CaseDelete
from automation.views import CaseHistory

from automation.views import SuiteNew
from automation.views import SuiteEdit
from automation.views import SuiteDelete
from automation.views import SuiteHistory

from automation.views import SchedulerNew
from automation.views import SchedulerEdit
from automation.views import SchedulerDelete
from automation.views import SchedulerHistory

from automation.views import CaseList
from automation.views import SuiteList
from automation.views import SchedulerList
from automation.views import RunList
from automation.views import DetailList
from automation.views import TestRunSuite
from automation.views import Requirement
from automation.views import TaskMonitor

urlpatterns = [
    url(r'^admin/jsi18n', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    url(r'^admin/', admin.site.urls),
    url(r'^test/', TestRunSuite),
    url(r'^dashboard/$', Dashboard.as_view()),
    url(r'^dashboard/case_new$', CaseNew.as_view(), name="case_new"),
    url(r'^dashboard/case_edit/(?P<id>[0-9]+)/$', CaseEdit.as_view(), name="case_edit"),
    url(r'^dashboard/case_delete/$', CaseDelete.as_view(), name="case_delete"),
    url(r'^dashboard/case_history/$', CaseHistory.as_view(), name="case_history"),

    url(r'^dashboard/suite_new$', SuiteNew.as_view(), name="suite_new"),
    url(r'^dashboard/suite_edit/(?P<id>[0-9]+)/$', SuiteEdit.as_view(), name="suite_edit"),
    url(r'^dashboard/suite_delete/$', SuiteDelete.as_view(), name="suite_delete"),
    url(r'^dashboard/suite_history/$', SuiteHistory.as_view(), name="suite_history"),

    url(r'^dashboard/scheduler_new$', SchedulerNew.as_view(), name="scheduler_new"),
    url(r'^dashboard/scheduler_edit/(?P<id>[0-9]+)/$', SchedulerEdit.as_view(), name="scheduler_edit"),
    url(r'^dashboard/scheduler_delete/$', SchedulerDelete.as_view(), name="scheduler_delete"),
    url(r'^dashboard/scheduler_history/$', SchedulerHistory.as_view(), name="scheduler_history"),

    url(r'^dashboard/case_list$', CaseList.as_view(), name="case_list"),
    url(r'^dashboard/suite_list$', SuiteList.as_view(), name="suite_list"),
    url(r'^dashboard/scheduler_list$', SchedulerList.as_view(), name="scheduler_list"),
    url(r'^dashboard/run_list$', RunList.as_view(), name="run_list"),
    url(r'^dashboard/detail_list$', DetailList.as_view(), name="detail_list"),

    url(r'^dashboard/task_monitor$', TaskMonitor.as_view(), name="task_monitor"),

    url(r'^markdownx/', include('markdownx.urls')),

    url(r'^requirement/requirement$', Requirement.as_view(), name="requirement"),
]
