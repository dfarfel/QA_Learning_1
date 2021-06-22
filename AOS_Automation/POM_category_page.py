from selenium import webdriver


class Category_Page:
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')

    def open_main_page(self):
        self.driver.find_element_by_css_selector('[class="ng-scope"][translate="HOME"]').click()

    def open_product_page(self, id):
        self.driver.find_element_by_css_selector(f'[id="{id}"]').click()

    def category_identification_element(self):
        return self.driver.find_element_by_css_selector('[class="categoryTitle roboto-regular sticky ng-binding"]').text

    def open_cart_page(self):
        self.driver.find_element_by_id("shoppingCartLink").click()
