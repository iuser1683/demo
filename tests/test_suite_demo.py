import unittest
from tests.home.all_tests import AllMainTest
from tests.home.navigation_tests import NavigationTests

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite()
unittest.TextTestRunner(verbosity=2).run(smokeTest)