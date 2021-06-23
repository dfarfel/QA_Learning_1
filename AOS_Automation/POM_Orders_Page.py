
from selenium import webdriver


class Orders_Page:
    def __init__(self, driver):
        self.driver = driver
        #self.driver = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')

    def order_number(self,order_place):
        orders_list=self.driver.find_elements_by_css_selector('[class="cover"]>table>tbody>tr>td>[class="ng-binding"]')
        if order_place>1:
            return orders_list[(order_place-1)+((order_place-1)*6)].text
        else:
            return orders_list[order_place-1].text