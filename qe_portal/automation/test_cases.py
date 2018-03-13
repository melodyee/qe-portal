# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from subprocess import call
from subprocess import check_output
from subprocess import CalledProcessError
from django.conf import settings

import os
import timeit

class Case(object):

    def __init__(self):
        self.model = None
        self.running = None

    def run(self):
        if self.model is None:
            print ("Error, No case model initilized for Case Obj.")
            return
        if self.running is None:
            print ("Error, No case running initilized for Case Obj.")
            return

        print "%s:%s Test Case Run! \n" % (self.model.name, self.model.type)
        print "cmd:%s, script:%s\n" % (self.model.cmd, self.model.script)

        start_time = timeit.default_timer()
        if self.model.script == "" or self.model.cmd == "":
            error_msg = "Invalid cmd or script! Replaced with \"sh -c \'false; exit 1\'\" \n"
            print error_msg
            retcode = call(["sh", "-c", "false; exit 2", ])
            print "Return Code:" + str(retcode) + "\n"
            self.running.ret_code = retcode
            self.running.error_msg = error_msg
        else:
            try:

                print "django base dir:" + settings.BASE_DIR
                #output = check_output([self.model.cmd, self.model.script, ], )

                abs_script_path = os.path.join(settings.BASE_DIR, self.model.script)
                print "script abs path:" + abs_script_path
                output = check_output([self.model.cmd, abs_script_path, ], )
                res = 0, output

            except CalledProcessError as e:
                res = e.returncode, e.message

            print "Return Code:" + str(res[0]) + "\n"
            print "Output:" + "\n" + res[1] + "\n"
            self.running.ret_code = res[0]
            self.running.error_msg = res[1]

        end_time = timeit.default_timer()
        self.running.run_time = end_time - start_time
        #self.running.save()
