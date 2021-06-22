
from selenium import webdriver

class Payment_Page:
    def __init__(self, driver):
        self.driver = driver
        #self.driver = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')

    def