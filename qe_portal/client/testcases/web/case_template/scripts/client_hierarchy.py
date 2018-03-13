import os

class ClientHierarchy:

    def __init__(self):
        ## Cases Dir
        self.script_dir = os.path.dirname(os.path.realpath(__file__))
        print "script_dir:", self.script_dir
        self.current_case_dir = os.path.abspath(os.path.join(self.script_dir, os.pardir))
        #print "current_case_dir:", self.current_case_dir
        self.data_dir = os.path.dirname(os.path.join(self.current_case_dir, "data/"))
        #print "data_dir:", self.data_dir
        self.current_cate_dir = os.path.abspath(os.path.join(self.current_case_dir, os.pardir))
        #print "current_cate_dir:", self.current_cate_dir
        self.testcase_dir = os.path.abspath(os.path.join(self.current_cate_dir, os.pardir))
        #print "testcase_dir:" , self.testcase_dir
        self.client_dir = os.path.abspath(os.path.join(self.testcase_dir, os.pardir))
        print "client_dir:", self.client_dir

        ## Output Dir
        self.output_dir = os.path.dirname(os.path.join(self.client_dir, "output/"))
        print "output_dir:", self.output_dir
        self.output_web_dir = os.path.abspath(os.path.join(self.output_dir, "web/"))
        #print "output_web_dir:", self.output_web_dir
        self.output_android_dir = os.path.abspath(os.path.join(self.output_dir, "android/"))
        #print "output_android_dir", self.output_android_dir
        self.output_ios_dir = os.path.abspath(os.path.join(self.output_dir, "ios/"))
        #print "output_ios_dir", self.output_ios_dir

        ## Tools Dir
        self.tools_dir = os.path.dirname(os.path.join(self.client_dir, "tools/"))
        print "tools_dir:", self.tools_dir
        self.web_tools_dir = os.path.dirname(os.path.join(self.tools_dir, "web/"))
        #print "web_tools_dir:", self.web_tools_dir
        self.android_tools_dir = os.path.dirname(os.path.join(self.tools_dir, "android/"))
        #print "android_tools_dir:", self.android_tools_dir
        self.ios_tools_dir = os.path.dirname(os.path.join(self.tools_dir, "ios/"))
        #print "ios_tools_dir:", self.ios_tools_dir


    def get_script_dir(self):
        return self.script_dir

    def get_testcase_dir(self):
        return self.testcase_dir

    def get_data_dir(self):
        return self.data_dir

    def get_output_dir(self):
        return self.output_dir

    def get_current_case_dir(self):
        return self.current_case_dir

    def get_tools_dir(self):
        return self.tools_dir

    def get_web_tools_dir(self):
        return self.web_tools_dir

    def get_android_tools_dir(self):
        return self.android_tools_dir

    def get_ios_tools_dir(self):
        return self.ios_tools_dir


