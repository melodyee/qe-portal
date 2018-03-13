from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

script_path = os.path.dirname(os.path.realpath(__file__))
webdriver_path = script_path + '/../../../../tools/web/selenium_driver/chromedriver'
print script_path, webdriver_path

driver = webdriver.Chrome(webdriver_path)  # Optional argument, if not specified will search path.


user = ""
pwd = ""
driver.get("http://www.facebook.com")

try:
    assert "FaceNOTbook" in driver.title
except Exception, e:
    print e
    driver.close()

elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.close()

