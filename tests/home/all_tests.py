from pages.home.child_pages import ChildPages
from pages.home.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import logging
import utilities.custom_logger as cl
import time
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AllMainTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.cp = ChildPages(self.driver)
        self.nav = NavigationPage(self.driver)
        self.ts = TestStatus(self.driver)

    def setUp(self):
        self.nav.navigate_add_remove()

    @pytest.mark.run(order=1)
    def test_add_element_001(self):
        test_result = self.cp.clickAddElement()
        if test_result is not None:
            self.log.info("Add remove element is present: PASS=>" + str(test_result))
            result=True
        else:
            self.log.error("Add Remove element is : FAIL")
            result = False
        self.ts.markFinal("Add Remove Element Present",result, "Is Present")




