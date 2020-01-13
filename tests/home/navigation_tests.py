from pages.home.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class NavigationTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.np = NavigationPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_01(self):
        self.log.info("*#" * 20)
        self.log.info("Finding total click-able elements in home page")
        self.log.info("*#" * 20)
        time.sleep(2)
        elementList = self.np.totalElementsInHomePage()
        total = len(elementList)
        self.log.info("Total Elements" + str(total))
        if total != 43:
            self.log.error("Test Failed")
            result = False
            self.ts.markFinal("Finding total elements in home page",result, "Total clickable elements")
        result = True
        self.log.info(" Total Elements test: PASS")
        self.ts.markFinal("Finding total elements in home page", result, "Total clickable elements")

    @pytest.mark.run(order=2)
    def test_02(self):
        self.log.info("*#" * 20)
        self.log.info("navigating to AB Test link")
        self.log.info("*#" * 20)
        time.sleep(2)
        self.np.navigate_AbTest()
        result = self.np.url_verify("http://the-internet.herokuapp.com/abtest")
        self.ts.markFinal("Navigated to AB Test",result, "Navigation to AB Test?")


