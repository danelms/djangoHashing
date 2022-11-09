from sys import hash_info
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from .forms import HashForm
import hashlib
from .models import Hash

class FunctionalTestCase(TestCase):
    #Opening behaviour
    def setUp(self):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

        self.browser = webdriver.Firefox(executable_path=r'D:\ARU Year 2\Web Programming\djangoHashing\env_laptop\Scripts\geckodriver.exe', options=options)

    #SITE TESTS

    #Must start with '_test'
    def test_homepage_displayed(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("Enter hash here:", self.browser.page_source)

    def test_hash_form(self):
        form = HashForm(data={'text':'hello'})
        self.assertTrue(form.is_valid())

    def test_hash_hello(self):
        #get homepage
        self.browser.get("http://localhost:8000")
        #find the text box to the data into
        text = self.browser.find_element_by_id("id_text")
        #enter hello to text box
        text.send_keys('hello')
        #click submit
        self.browser.find_element_by_name('submit').click()
        #check for correct hash value
        self.assertIn('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', self.browser.page_source)

    def test_hash_function_works(self):
        #create hash from 'hello'
        text_hash = hashlib.sha256('hello'.encode('utf-8')).hexdigest()
        #check it's equal to actual hash value
        self.assertEqual('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', text_hash)

    #DATABASE TESTS

    def storeHashOfHello(self):
        #Create Hash object
        hashObj = Hash()
        hashObj.text = 'hello'
        hashObj.hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'

        #Store in database
        hashObj.save()
        return hashObj

    def test_hash_object(self):
        hashObj = self.storeHashOfHello()

        #Retrieve from database
        hashPulled = Hash.objects.get(hash='2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        #confirm the data is correct
        self.assertEqual(hashPulled.text, hashObj.text)

    def test_view_of_hash(self):
        self.storeHashOfHello()
        response = self.client.get('/hash/2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        self.assertContains(response, 'hello')

    #Closing behaviour
    def tearDown(self):
        self.browser.quit()



