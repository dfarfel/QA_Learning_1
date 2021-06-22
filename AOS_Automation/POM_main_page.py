from selenium import webdriver


class Main_Page:
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')

    def open_category_page(self, category):
        self.driver.find_element_by_css_selector(f'[id="{category}Txt"]').click()

    def open_user_login_page(self):
        self.driver.find_element_by_id('menuUserSVGPath').click()

    def open_cart_page(self):
        self.driver.find_element_by_id("shoppingCartLink").click()

    def main_page_identification_element(self):
        self.driver.find_element_by_css_selector('')
