import unittest
from appium import webdriver
import os


class test_android_login(unittest.TestCase):
    dc = {}
    driver = None

    def setUp(self):
        # This is the Application and ‘app’ desired capability to specify a path to Appium.
        self.dc['app'] = os.path.abspath('app-release.apk')
        # appPackage and appActivity  desired capability specify app details to Appium
        self.dc['appPackage'] = "com.teamway"
        self.dc['appActivity'] = ".LoginActivity"
        # platformName desired capability specify platform detail to Appium
        self.dc['platformName'] = 'Android'
        # deviceName desired capability specify the device id detail to Appium
        # device id is got from running adb devices command in PC
        self.dc['deviceName'] = 'emulator-5554'
        self.dc['appWaitActivity'] = ".activities.*"
        # Creating the Driver by passing Desired Capabilities.
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)

    def test_login(self):
        pass
        # if len(self.driver.find_elements_by_xpath("//*[@text='OK']")) > 0:
        #     self.driver.find_element_by_xpath("//*[@text='OK']").click();
        # # Find location of Elements and perform action.
        # self.driver.find_element_by_xpath("//*[@text='Username']").send_keys('company')
        # self.driver.find_element_by_xpath("//*[@text='Password']").send_keys('company')
        # self.driver.find_element_by_xpath("//*[@text='Login']").click()
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()