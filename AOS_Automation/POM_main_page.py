from AOS_Automation.Ecxel_prog import Excel_AOS
from selenium import webdriver


class Main_Page:
    def __init__(self, driver):
        self.driver = driver
        #self.driver = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')
        self.excel = Excel_AOS()

    def open_category_page_product(self,category):
        self.driver.find_element_by_css_selector(f'[id="{category}Txt"]').click()

    def open_user_login_page(self):
        self.driver.find_element_by_id('menuUserSVGPath').click()

    def type_username(self):
        self.driver.find_element_by_name('username').send_keys(self.excel.exist_account('username',6))

    def type_password(self):
        self.driver.find_element_by_name('password').send_keys(self.excel.exist_account('password',6))

    def sign_in_click(self):
        self.driver.find_element_by_id('sign_in_btnundefined').click()

    def open_cart_page(self):
        self.driver.find_element_by_id("shoppingCartLink").click()





