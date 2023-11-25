import allure
from selenium.common.exceptions import WebDriverException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Taking a screenshot on test failure")
    def take_screenshot_on_failure(self, test_name):
        try:
            allure.attach(self.driver.get_screenshot_as_png(), name=test_name, attachment_type=allure.attachment_type.PNG)
        except WebDriverException as e:
            print("Failed to take screenshot:", e)
