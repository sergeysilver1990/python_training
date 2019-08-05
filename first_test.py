from selenium import webdriver
import unittest

def is_alert_present(wd):
    try:
        wd.swithc_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver()
        self.wd