from pages import baseElement
from selenium.webdriver.common.by import By

class loginPage(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def find_username(self, text):
        locator = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.View')
        return baseElement(
            driver = self.driver,
            by = locator[0],
            value = locator[1],
        )


    def find_password(self, text):
        pass

    def click_submit(self, text):
        button = self.driver.find_element_by_id('the_id')
        button.click()
        return None