# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import Queue
import datetime

from django.core.mail import send_mail

from automation.schedulers import Scheduler

class Suite(object):

    def __init__(self):
        self.name = "Test Suite Untitled"
        self.queue = Queue.Queue()
        self.visitor = []
        self.scheduler = Scheduler()
        self.createTime = datetime.datetime.now()
        self.executeTime = datetime.datetime.now()
        self.emails = []

    def addTask(self, tc):
        self.queue.put(tc)

    def getTask(self):
        return self.queue.get()

    def countTask(self):
        return self.queue.qsize()

    def scedule(self):
        self.scheduler.schedule(self.queue)

    def exportToJson(selfs):
        print "serialize to jason file."
        pass

    def readFromJson(self, context):
        pass

    def format_result(self):
        return "pass"
        pass

    def send_result(self):
        content = self.format_result()
        send_mail(
            'Automation Result:' + self.name + ":" + str(self.executeTime),
            content,
            'zerozeroautomation@gmail.com',
            ['libaichao@zerozero.cn'],
            fail_silently=False,
        )
        pass




