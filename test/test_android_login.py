import unittest
from appium import webdriver
import os
from helpers import report_to_sauce, take_screenshot_and_logcat, ANDROID_BASE_CAPS, EXECUTOR
import time
# import test.pages.baseElement
# import test.pages.loginPage
from pages import baseElement
from pages import loginPage

# import test.

class test_android_login(unittest.TestCase):
    dc = {}
    # driver = None

    # def setUp(self):
    #     # This is the Application and ‘app’ desired capability to specify a path to Appium.
    #     self.dc['app'] = os.path.abspath('../app-release.apk')
    #     self.dc['platformName'] = 'Android'
    #     # device id is got from running adb devices command in PC
    #     self.dc['deviceName'] = 'emulator-5554'
    #     self.dc['appWaitActivity'] = "com.teamway.MainActivity"
    #     # Creating the Driver by passing Desired Capabilities.
    #     self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)

    def test_login(self):
       login = loginPage(driver)

       login.find_username.click()
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()