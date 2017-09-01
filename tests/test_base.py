from tests.testbase import FunctionalTest

class TestBase(FunctionalTest):
    def test_base1(self):

        self.browser.get("http://localhost:8000")

