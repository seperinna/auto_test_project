from selenium import webdriver
from browser_driver import openBrowser
import unittest

class TestEnv(unittest.TestCase):
    def setUp(self):
        self.driver = openBrowser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()


