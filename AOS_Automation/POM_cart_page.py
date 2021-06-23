
from selenium import webdriver


class Cart_Page:
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')


    def click_edit_button(self, place_number):
        edit_list = self.driver.find_elements_by_css_selector('[class="edit ng-scope"]')
        edit_list[place_number - 1].click()

    def quantity_element(self, place_number):
        quantity_list = self.driver.find_elements_by_css_selector(
            '[class="smollCell quantityMobile"]>[class="ng-binding"]')
        return quantity_list[place_number-1]

    def cart_is_empty_element(self):
        self.driver.find_element_by_css_selector('[class="roboto-bold ng-scope"]')

    def cart_is_empty_element_txt(self):
        return self.driver.find_element_by_css_selector('[class="roboto-bold ng-scope"]').text
