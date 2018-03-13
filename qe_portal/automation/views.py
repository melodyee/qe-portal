# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import subprocess
import os

from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.forms import modelform_factory
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.conf import settings

from celery.result import AsyncResult
from qe_portal.celery import app

# Create your tests here.
from test_suites import Suite
from test_cases import Case

from automation.forms import CaseForm
from automation.forms import SuiteForm
from automation.forms import SchedulerForm

from automation.models import CaseModel
from automation.models import SuiteModel
from automation.models import SchedulerModel

from automation.models import SuiteRunningModel

from automation.schedulers import SchedulerAtOnce

from automation.models import RequirementModel
from automation.forms import RequirementForm


# Create your views here.


class Dashboard(View):
    def get(self, request):
        return render(request, 'dashboard/dashboard.html')

    def post(self, request):
        return render(request, 'dashboard/dashboard.html')


class CaseNew(View):
    def get(self, request):
        form = CaseForm()
        return render(request, 'dashboard/case_new.html', {'form': form})

    def post(self, request):
        form = CaseForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            new_case = form.save(commit=False)
            print new_case
            new_case.save()

            # process the data in form.cleaned_data as required
            # ...

#        subject = form.cleaned_data['subject']
#        message = form.cleaned_data['message']
#        sender = form.cleaned_data['sender']
#        cc_myself = form.cleaned_data['cc_myself']
#        recipients = ['info@example.com']
#        #send_mail(subject, message, sender, recipients)
#        return HttpResponseRedirect('/thanks/')
#
        #form = CaseForm()
        form = modelform_factory(CaseModel, fields='__all__')
        return render(request, 'dashboard/case_new.html', {'form': form})

class CaseEdit(View):

    def get(self, request, id):
        if id > 0:
            case = CaseModel.objects.get(pk=id)
            print case
            form = CaseForm(instance=case)
            print form
            return render(request,'dashboard/case_edit.html', {'form': form, 'id': id})
        else:
            return HttpResponse("Edit Case Error, Wrong ID Return!")


    def post(self, request, id):
        if id > 0:
            print request.POST
            print id
            print "post:update case id:", id
            instance = get_object_or_404(CaseModel, id=id)
            form = CaseForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
            return render(request, 'dashboard/case_edit.html', {'form': form, 'id':id})
        else:
            return HttpResponse("Update Case Error! Wrong Case ID!")

class CaseDelete(View):

    def get(self, request):
        data = {'id': id, 'ret': False}
        return HttpResponse(json.dumps(data), content_type='application/json')

    def post(self, request):
        if 'id' in request.POST:
            id = request.POST['id']
            if id > 0:
                instance = CaseModel.objects.get(id=id)
                instance.delete()
                print "Post, Case Deleted:", id
                data = {'id': id, 'ret': True}
                return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            data = {'id': id, 'ret': False}
            return HttpResponse(json.dumps(data), content_type='application/json')

class CaseHistory(View):

    def get(self, request):
        data = {'id': id, 'h_list': []}
        return HttpResponse(json.dumps(data), content_type='application/json')

    def post(self, request):
        if 'id' in request.POST:
            id = request.POST['id']
            if id > 0:
                instance = CaseModel.objects.get(id=id)
                h_list = instance.history.all()
                print "Get Case Deleted:", id
                h_list = serializers.serialize('json', h_list)
                h_list_dict = json.loads(h_list)
                print h_list_dict
                data = dict({'id': id}.items() + {'h_list': h_list_dict}.items())
                return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            data = {'id': id, 'h_list': []}
            return HttpResponse(json.dumps(data), content_type='application/json')


class SuiteNew(View):
    def get(self, request):
        form = SuiteForm()
        return render(request, 'dashboard/suite_new.html', {'form': form})

    def post(self, request):
        form = SuiteForm(request.POST)
        if form.is_valid():
            new_suite = form.save(commit=True)
            print "suite case number:", new_suite.cases.count()
        form = modelform_factory(SuiteModel, fields= '__all__')
        return render(request, 'dashboard/suite_new.html', {'form': form})


class SuiteEdit(View):

    def get(self, request, id):
        if id > 0:
            suite = SuiteModel.objects.get(pk=id)
            print suite
            form = SuiteForm(instance=suite)
            print form
            return render(request, 'dashboard/suite_edit.html', {'form': form, 'id': id})
        else:
            return HttpResponse("Edit Suite Error, Wrong ID Return!")


    def post(self, request, id):
        if id > 0:
            print request.POST
            print id
            print "post:update case id:", id
            instance = get_object_or_404(SuiteModel, id=id)
            form = SuiteForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
            return render(request, 'dashboard/suite_edit.html', {'form': form, 'id': id})
        else:
            return HttpResponse("Update Suite Error! Wrong ID!")


class SuiteDelete(View):

    def get(self, request):
        data = {'id': id, 'ret': False}
        return HttpResponse(json.dumps(data), content_type='application/json')

    def post(self, request):
        if 'id' in request.POST:
            id = request.POST['id']
            if id > 0:
                instance = SuiteModel.objects.get(id=id)
                instance.delete()
                print "Post, Case Deleted:", id
                data = {'id': id, 'ret': True}
                return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            data = {'id': id, 'ret': False}
            return HttpResponse(json.dumps(data), content_type='application/json')


class SuiteHistory(View):

    def get(self, request):
        data = {'id': id, 'h_list': []}
        return HttpResponse(json.dumps(data), content_type='application/json')

    def post(self, request):
        if 'id' in request.POST:
            id = request.POST['id']
            if id > 0:
                instance = SuiteModel.objects.get(id=id)
                h_list = instance.history.all()
                print "Get Case Deleted:", id
                h_list = serializers.serialize('json', h_list)
                h_list_dict = json.loads(h_list)
                print h_list_dict
                data = dict({'id': id}.items() + {'h_list': h_list_dict}.items())
                return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            data = {'id': id, 'h_list': []}
            return HttpResponse(json.dumps(data), content_type='application/json')


class SchedulerNew(View):
    def get(self, request):
        form = SchedulerForm()
        return render(request, 'dashboard/scheduler_new.html', {'form': form})

    def post(self, request):
        form = SchedulerForm(request.POST)
        if form.is_valid():
            new_model = form.save(commit=False)
            print new_model
            new_model.save()
        form = modelform_factory(SchedulerModel, exclude=["create_time", ])
        return render(request, 'dashboard/scheduler_new.html', {'form': form})

class SchedulerEdit(View):

    def get(self, request, id):
        if id > 0:
            model = SchedulerModel.objects.get(pk=id)
            print model
            form = SchedulerForm(instance=model)
            print form
            return render(request, 'dashboard/scheduler_edit.html', {'form': form, 'id': id})
        else:
            return HttpResponse("Edit Scheduler Error, Wrong ID Return!")


    def post(self, request, id):
        if id > 0:
            print request.POST
            print id
            print "post:update case id:", id
            instance = get_object_or_404(SchedulerModel, id=id)
            form = SchedulerForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
            return render(request, 'dashboard/scheduler_edit.html', {'form': form, 'id': id})
        else:
            return HttpResponse("Update Scheduler Error! Wrong ID!")


class SchedulerDelete(View):

    def get(self, request):
        data = {'id': id, 'ret': False}
        return HttpResponse(json.dumps(data), content_type='application/json')

    def post(self, request):
        if 'id' in request.POST:
            id = request.POST['id']
            if id > 0:
                instance = SchedulerModel.objects.get(id=id)
                instance.delete()
                print "Post, Scheduler Deleted:", id
                data = {'id': id, 'ret': True}
                return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            data = {'id': id, 'ret': False}
            return HttpResponse(json.dumps(data), content_type='application/json')


class SchedulerHistory(View):

    def get(self, request):
        data = {'id': id, 'h_list': []}
        return HttpResponse(json.dumps(data), content_type='application/json')

    def post(self, request):
        if 'id' in request.POST:
            id = request.POST['id']
            if id > 0:
                instance = SchedulerModel.objects.get(id=id)
                h_list = instance.history.all()
                print "Get Scheduler Deleted:", id
                h_list = serializers.serialize('json', h_list)
                h_list_dict = json.loads(h_list)
                print h_list_dict
                data = dict({'id': id}.items() + {'h_list': h_list_dict}.items())
                return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            data = {'id': id, 'h_list': []}
            return HttpResponse(json.dumps(data), content_type='application/json')


class CaseList(View):

    def get(self, request):
        cases = CaseModel.objects.all()
        return render(request, 'dashboard/case_list.html', {'cases':cases})

    def post(self, request):
        return render(request, 'dashboard/case_list.html')

class SuiteList(View):

    def get(self, request):
        suites = SuiteModel.objects.all()
        return render(request, 'dashboard/suite_list.html', {'suites':suites})

    def post(self, request):
        return render(request, 'dashboard/suite_list.html')

class Scheduler4UI(object):
    def __init__(self, sched_model):
        self.sched_model = sched_model
        self.latest_running = None
        self.latest_progress = 0
        self.latest_pass_num = 0
        self.latest_fail_num = 0

    def update(self):
        self.latest_running = self.sched_model.suiterunningmodel_set.all().order_by('-id')[0]
        self.get_progress()
        self.get_passfail()

    def get_progress(self):
        self.latest_progress = self.latest_running.progress

    def get_passfail(self):
        self.latest_pass_num = 0
        self.latest_fail_num = 0
        for item in self.latest_running.case_runnings.all():
            if item.ret_code == 0:
                self.latest_pass_num = self.latest_pass_num + 1
            else:
                self.latest_fail_num = self.latest_fail_num + 1


class SchedulerList(View):

    def PackScheduleUI(self, schedulers):
        ui_list = []
        for item in schedulers:
            s4ui = Scheduler4UI(item)
            #s4ui.update()
            ui_list.append(s4ui)
        return ui_list


    def poll_state(self, sched_run_id):

        progress = 0

        try:
            print "sched_run_id:", sched_run_id
            sched_running = SuiteRunningModel.objects.get(pk=sched_run_id)

        except ObjectDoesNotExist:
            print("Schedule running %s doesn't exist." % sched_run_id)
            return progress

        case_runnings = sched_running.case_runnings
        case_total = case_runnings.count()
        case_finished = 0
        for c_r in case_runnings.all():
            res = AsyncResult(c_r.task_id, app=app)
            data = res.result or res.state
            if data == 'SUCCESS' or data == 'FAILURE':
                case_finished = case_finished + 1
                print(json.dumps(data))
                sched_running.progress = case_finished * 100.0 / case_total# percentage

            ''' For Debug 
            print "task_scheduled_id:" + c_r.task_id
            print res.get(timeout=c_r.case.timeout, propagate=False)
            print "task execute result:" + res.status
            '''
        sched_running.save()
        progress = sched_running.progress
        return progress

    def get(self, request):
        print ("Get:")
        if request.is_ajax and request.GET:
            """ A view to report the progress to the user """
            if 'sched_id' in request.GET and 'sched_run_id' in request.GET:
                sched_id = request.GET['sched_id']
                sched_run_id = request.GET['sched_run_id']
                print ("Poll state called!, sched_id:%s, sched_run_id:%s", (sched_id, sched_run_id))
                progress = self.poll_state(sched_run_id)
                data = ({'sched_id':sched_id, 'sched_run_id':sched_run_id, 'sched_progress':progress})
                print data
                return HttpResponse(json.dumps(data), content_type='application/json')
            else:
               schedulers = SchedulerModel.objects.all()
               schedulerUIs = self.PackScheduleUI(schedulers)
               return render(request, 'dashboard/scheduler_list.html', {'schedulerUIs':schedulerUIs})
        else:
            schedulers = SchedulerModel.objects.all()
            schedulerUIs = self.PackScheduleUI(schedulers)
            for item in schedulerUIs:
                print item.sched_model.pk, item.sched_model.name
            return render(request, 'dashboard/scheduler_list.html', {'schedulerUIs':schedulerUIs})

    def post(self, request):
        print ("Post:")
        if request.is_ajax() and request.POST:
            message = "This is ajax, and POST"
            print message
            sched_id = request.POST.get('id')
            print sched_id
            sch = SchedulerAtOnce()
            sch.schedule(sched_id)

            import json
            response = json.dumps({'sched_id': sched_id,'sched_run_id': sch.running.pk})
            return HttpResponse(response, content_type='application/json')

            # if django version >1.7
            #from django.http import JsonResponse
            #return JsonResponse({'foo': 'bar'})
        else:
            message = "Not ajax. POST"
            print message

        schedulers = SchedulerModel.objects.all()
        schedulerUIs = self.PackScheduleUI(schedulers)
        for item in schedulerUIs:
            print item.sched_model.pk, item.sched_model.name
        return render(request, 'dashboard/scheduler_list.html', {'schedulerUIs':schedulerUIs})


class RunList(View):
    def post(self, request):
        runs = SuiteRunningModel.objects.all().order_by('-id')
        return render(request, 'dashboard/suite_run_list.html', {'runs':runs})

    def get(self, request):
        runs = SuiteRunningModel.objects.all().order_by('-id')
        return render(request, 'dashboard/suite_run_list.html', {'runs':runs})


class DetailList(View):

    '''
    def post(self, request):
        if 'id' in request.POST:
            id = request.POST['id']
            if id > 0:
                suite_run = SuiteRunningModel.objects.get(pk=id)
                h_list = suite_run.case_runnings.all()
                print "Get Scheduler Deleted:", id
                h_list = serializers.serialize('json', h_list)
                h_list_dict = json.loads(h_list)
                print h_list_dict
                data = dict({'id': id}.items() + {'h_list': h_list_dict}.items())
                return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            data = {'id': id, 'h_list': []}
            return HttpResponse(json.dumps(data), content_type='application/json')

    '''

    def post(self, request):
        if 'id' in request.POST:
            id = request.POST['id']
            suite_run = SuiteRunningModel.objects.get(pk=id)
        else:
            suite_run = SuiteRunningModel.objects.all().order_by('-id')[0]

        runs = suite_run.case_runnings.all()
        return render(request, 'dashboard/case_run_list.html', {'runs': runs})

    def get(self, request):
        if 'id' in request.GET:
            id = request.GET['id']
            suite_run = SuiteRunningModel.objects.get(pk=id)
            runs = suite_run.case_runnings.all()
        else:
            try:
                suite_run = SuiteRunningModel.objects.all().order_by('-id')[0]
                runs = suite_run.case_runnings.all()
            except IndexError as e:
                print e
                runs = []
        return render(request, 'dashboard/case_run_list.html', {'runs': runs})


class Requirement(View):
    def get(self, request):
        form = RequirementForm()
        return render(request, 'requirement/requirement.html', {'form': form})

    def post(self, request):
        form = RequirementForm(request.POST)
        if form.is_valid():
            model = RequirementModel()
            model.Requirement = form.declared_fields('ReqField')
            model.save()
        return render(request, 'requirement/requirement.html', {'form': form})


class TaskMonitor(View):
    def start_flower(self):
        print settings.BASE_DIR
        os.system("cd %s" % settings.BASE_DIR)
        sudoPassword = '1234'
        # command = 'celery flower -A qe_port --address=0.0.0.0 --port=5555'
        command = 'celery flower -A localhost --address=0.0.0.0 --port=5555'
        p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
        print p
        #os.popen("sudo -S %s" % (command), 'w').write('mypass')
        #output = subprocess.check_output("celery flower - A qe_portal --address=127.0.0.1 --port=5555")

    def get(self, request):
        # Don't need to call the process here, replaced with run a shell command in server by ops.
        #self.start_flower()
        return HttpResponseRedirect("http://qe-port:5555/")

    def post(self, request):
        # Don't need to call the process here, replaced with run a shell command in server by ops.
        #self.start_flower()
        return HttpResponseRedirect("http://qe-port:5555/")


def TestRunSuite(request):

    suite = Suite()

    t1 = Case()
    t1.type = Case.TYPE['web']
    t1.name = "case-1"
    t1.script = "/Volumes/data/real/virtualenvs/qe_portal_env/qe_portal/client/testcases/web/case-1/script.py"
    t1.cmd = "python"

    t4 = Case()
    t4.type = Case.TYPE['web']
    t4.name = "case-2"
    t4.script = "/Volumes/data/real/virtualenvs/qe_portal_env/qe_portal/client/testcases/web/case-2/script.py"
    t4.cmd = "python"
    t4.timeout = 150

    t2 = Case()
    t2.type = Case.TYPE["android"]

    t3 = Case()
    t3.type = Case.TYPE["ios"]
    t3.timeout = 300

    suite.addTask(t1)
    suite.addTask(t2)
    suite.addTask(t3)
    suite.addTask(t4)

    suite.scedule()
    print "send result:"
    suite.send_result()

    return HttpResponse("OK")

