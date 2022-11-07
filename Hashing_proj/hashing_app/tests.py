from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class FunctionalTestCase(TestCase):

    def setUp(self):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

        self.browser = webdriver.Firefox(executable_path=r'D:\ARU Year 2\Web Programming\djangoHashing\env_laptop\Scripts\geckodriver.exe', options=options)

    #Must start with '_test'
    def test_install_worked(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("install", self.browser.page_source)

    def tearDown(self):
        self.browser.quit()



