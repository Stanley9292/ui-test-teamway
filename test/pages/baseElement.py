from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

ANDROID_BASE_CAPS = {
    'app': os.path.abspath('app-release.apk'),
    'automationName': 'UIAutomator2',
    'platformName': 'Android',
    # 'platformVersion': os.getenv('emulator-5554') or '8.0',
    'deviceName':"emulator-5554",
}

# created a wrapper class over selenium that can find an element by any type of locator
class BaseElement(object):
    def __init__(self, driver, value, by):
        # This is the Application and ‘app’ desired capability to specify a path to Appium.
        self.dc['app'] = os.path.abspath('../app-release.apk')
        self.dc['platformName'] = 'Android'
        # device id is got from running adb devices command in PC
        self.dc['deviceName'] = 'emulator-5554'
        self.dc['appWaitActivity'] = "com.teamway.MainActivity"

        # Creating the Driver by passing Desired Capabilities.
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)
        self.value = value
        self.by = by
        self.locator = (self.by, self.value)

        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(
            driver, 10).until(EC.visibility_of_element_located(
                locator=self.locator
            ))
        self.web_element = element
        return None

    def click(self):
        element = WebDriverWait(
            driver, 10).until(EC.element_to_be_clickable(
                locator=self.locator
            ))
        element.click()
        return None

    def text(self):
        text = self.web_element.text
        return text