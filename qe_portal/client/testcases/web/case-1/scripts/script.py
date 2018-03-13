import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import sys

import client_hierarchy as ch


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        ch_obj = ch.ClientHierarchy()
        sys.path.append(ch_obj.get_web_tools_dir())
        webdriver_path = os.path.join(ch_obj.get_web_tools_dir(), "selenium_driver/chromedriver")
        print "Case Setup..."
        print "chromedriver path:", webdriver_path
        self.driver = webdriver.Chrome(executable_path=webdriver_path)  # Optional argument, if not specified will search path.

    def test_search_in_python_org(self):
        print "Case Running..."
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()
        print "Case Done!"

if __name__ == "__main__":
    unittest.main()
