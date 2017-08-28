import sys
import os
from functools import wraps

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.conf import settings
from selenium import webdriver
import unittest


class FunctionalTest(unittest.TestCase):

    def setUp(self):
        if sys.platform == 'darwin':
            #project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
            #repo_root = os.path.dirname(project_root)
            #sys.path.append(os.path.join(repo_root, 'dev'))
            from download_chromedriver import get_chromedriver_path
            chrome_path = get_chromedriver_path()
            if chrome_path is False:
                raise SystemExit
            self.browser = webdriver.Chrome(chrome_path)
        else:
            self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
