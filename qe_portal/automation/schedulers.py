from django.utils import timezone
from celery.result import AsyncResult
from qe_portal.celery import app
from threading import Thread
import time

from automation.tasks import run_web_task
from automation.tasks import run_android_task
from automation.tasks import run_ios_task

from automation.models import CaseRunningModel
from automation.models import SchedulerModel
from automation.models import SuiteRunningModel
from automation.test_cases import Case

def getResult():
    pass

class BaseThread(Thread):
    def __init__(self, callback=None, callback_args=None, *args, **kwargs):
        target = kwargs.pop('target')
        super(BaseThread, self).__init__(target=self.target_with_callback, *args, **kwargs)
        self.callback = callback
        self.method = target
        self.method_args = args
        self.callback_args = callback_args

    def target_with_callback(self, id):
        print id
        self.method(id)
        if self.callback is not None:
            self.callback(*self.callback_args)

def getCaseRunningResult(id):
    print "called getCaseRunningResult"
    # do any things here
    print "thread start successfully and sleep for 5 seconds"
    running = SuiteRunningModel.objects.get(pk=id)
    #running = SuiteRunningModel.objects.all().order_by('-id')[0]
    print running.pk
    case_account = running.case_runnings.count()
    print "case_account:", case_account
    case_finished = 0
    case_failure = 0
    for item in running.case_runnings.all():
        print item
        print "task-id:", item.task_id
        print "get-result-timeout:", item.case.timeout
        res = AsyncResult(item.task_id, app=app)
        tc_running = res.get(timeout=item.case.timeout, propagate=False)
        print "tc_running", tc_running
        item.ret_code = tc_running.ret_code
        if item.ret_code <> 0:
            case_failure += 1
        print "hahahahahhahahahhahah", tc_running.error_msg
        item.error_msg = tc_running.error_msg
        item.save()
        case_finished += 1

    if case_failure == 0 and case_finished > 0:
        running.ret = 0
        print "set running result:", running.ret
    else:
        print "set running result:", running.ret
        running.ret = 1
    running.progress = case_finished * 100 / case_account
    running.status = "Completed"
    running.save()

def getRunningResultDone_callback(param1, param2):
    # this is run after your thread end
    print "callback function called"
    print "{} {}".format(param1, param2)


class Scheduler(object):

    def __init__(self):
        self.running = None     #suite_running
        self.model = None       #schedule model


    def run(self):
        if self.model == None:
            return

        case_set = self.model.suite.cases.all()
        # For Debugging
        '''
        for case_m in case_set:
            print case_m.name
            print case_m.script
            print case_m.type
            print case_m.cmd
            print case_m.description
        '''
        self.running = SuiteRunningModel()
        self.running.suite = self.model.suite
        self.running.start_time = timezone.now()
        self.running.status = 'Running'
        self.running.save()

        for case_m in case_set:
            case = Case()
            case.model = case_m
            case.running = CaseRunningModel()
            case.running.case = case.model
            case.running.save()

            if case_m.type == "web":
                res = run_web_task.delay(case)
            elif case_m.type == "android":
                res = run_android_task.delay(case)
            elif case_m.type == "ios":
                res = run_ios_task.delay(case)
            else:
                print ("Case Type Error!!!")

            print res.id + "," + str(case_m.timeout)
            case.running.task_id = res.id
            case.running.save()
            self.running.case_runnings.add(case.running)

        self.running.status = 'Scheduled'
        self.running.save()

        thread = BaseThread(
            name='GetSuiteRuningResult',
            target=getCaseRunningResult,
            callback=getRunningResultDone_callback,
            callback_args=("hello", "world"),
            args=(self.running.pk,),
        )

        thread.start()


class SchedulerAtOnce(Scheduler):
    def schedule(self, id):
        self.model = SchedulerModel.objects.get(pk=id)
        self.run()

class SchedulerRepeat(Scheduler):
    pass;

class SchedulerReserved(Scheduler):
    pass;
