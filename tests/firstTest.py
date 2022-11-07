from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

browser = webdriver.Firefox(executable_path=r'D:\ARU Year 2\Web Programming\djangoHashing\env_laptop\Scripts\geckodriver.exe', options=options)

browser.get("http://localhost:8000")

assert browser.page_source.find('install')

#browser = webdriver.Edge()
#browser.get("http://localhost:8000")
#assert browser.page_source.find('install')