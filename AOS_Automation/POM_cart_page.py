from AOS_Automation.Ecxel_prog import Excel_AOS
from selenium import webdriver

class Cart_Page:
    def __init__(self, driver):
        self.driver = driver
        #self.driver = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')
        self.excel = Excel_AOS()

    def
