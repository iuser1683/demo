import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class ChildPages(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _add_button = "//div[@id='content']//button[text()='Add Element']"
    _delete_button = "//div[@id='content']//button[text()='Delete']"

    def clickAddElement(self):
        element = self.waitForElement(self._add_button, "xpath")
        element.click()
        delete_button = self.waitForElement(self._delete_button,"xpath")
        el2 = self.elementPresenceCheck(self._delete_button,"xpath")
        self.log.info("ELement List" + str(delete_button) + str(el2))
        # delete_button.click()
        return el2
        # element = self.isElementPresent(self._add_button, "xpath")

    def clickDeleteElement(self):
        element = self.waitForElement(self._add_button, "xpath")
        element.click()
        delete_button = self.waitForElement(self._delete_button,"xpath")
        delete_button.click()
        return self.isElementPresent(delete_button)



