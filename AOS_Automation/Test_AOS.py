from selenium import webdriver
from unittest import TestCase
from AOS_Automation.POM_main_page import Main_Page
from AOS_Automation.Ecxel_prog import Excel_AOS
from AOS_Automation.POM_category_page import Category_Page
from AOS_Automation.POM_product_page import Product_Page
from AOS_Automation.POM_cart_page import Cart_Page
import time


class Test_AOS(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')
        self.driver.get('https://www.advantageonlineshopping.com/#/')
        self.driver.implicitly_wait(20)
        self.main_page = Main_Page(self.driver)
        self.categ_page = Category_Page(self.driver)
        self.prod_page = Product_Page(self.driver)
        self.cart_page = Cart_Page(self.driver)
        self.exel = Excel_AOS()

    def test_6(self):
        self.main_page.open_category_page(self.exel.product_1('category', 6))
        self.categ_page.open_product_page(self.exel.product_1('id', 6))
        self.prod_page.add_product_quantity(self.exel.product_1('quantity', 6))
        self.prod_page.click_add_to_cart_btn()
        self.prod_page.open_main_page()

        self.main_page.open_category_page(self.exel.product_2('category', 6))

        self.categ_page.open_product_page(self.exel.product_2('id', 6))

        self.prod_page.add_product_quantity(self.exel.product_2('quantity', 6))
        self.prod_page.click_add_to_cart_btn()
        self.prod_page.open_cart_page()

        self.cart_page.click_edit_button(1)

        self.prod_page.dif_product_quantity(4)

        self.prod_page.click_add_to_cart_btn()

        self.cart_page.click_edit_button(2)

        self.prod_page.dif_product_quantity(2)
        self.prod_page.click_add_to_cart_btn()

        self.assertEqual(self.cart_page.quantity_element(1).text, str((int((self.exel.product_1('quantity', 6)) - 4))))
        self.assertEqual(self.cart_page.quantity_element(2).text, str((int((self.exel.product_2('quantity', 6)) - 2))))

    def test_7(self):
        self.main_page.open_category_page(self.exel.product_1('category', 7))
        self.categ_page.open_product_page(self.exel.product_1('id', 7))
        self.prod_page.click_add_to_cart_btn()
        self.prod_page.open_category_page()
        identofocation_category = self.categ_page.category_identification_element()
        self.categ_page.open_main_page()
        current_url = self.driver.current_url
        self.assertEqual(identofocation_category, "TABLETS")
        self.assertEqual(current_url, 'https://www.advantageonlineshopping.com/#/')

    def tearDown(self):
        time.sleep(5)
        self.driver.close()
