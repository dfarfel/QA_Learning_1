from AOS_Automation.Ecxel_prog import Excel_AOS
from selenium import webdriver

class Product_Page:
    def __init__(self, driver):
        self.driver = driver
       # self.driver = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')
        self.excel = Excel_AOS()

    def click_add_to_cart_btn(self):
        self.driver.find_element_by_css_selector("[name='save_to_cart']").click()

    def add_product_quantity(self,quantity):
        for i in range(int(quantity)-1):
            self.driver.find_element_by_css_selector('[class="plus"]').click()

    def open_main_page(self):
        self.driver.find_element_by_css_selector('[class="ng-scope"][translate="HOME"]').click()

    def open_cart_page(self):
        self.driver.find_element_by_id("shoppingCartLink").click()
