# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from automation.test_config import TEST_CONFIG

# Create your tests here.

from test_suites import Suite
from test_cases import Case



class  TCSuiteTestCases(TestCase):

    def setUp(self):
        pass


    def test_RunSuiteTest(self):

        suite = Suite()

        t1 = Case()
        t1.type = Case.TYPE['web']
        t1.name = "case-1"
        t1.script = "/Volumes/data/real/virtualenvs/git/qe_portal_env/qe_portal/client/testcases/web/case-1/script.py"
        t1.cmd = "python"

        t4 = Case()
        t4.type = Case.TYPE['web']
        t4.name = "case-2"
        t4.script = "/Volumes/data/real/virtualenvs/git/qe_portal_env/qe_portal/client/testcases/web/case-2/script.py"
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

