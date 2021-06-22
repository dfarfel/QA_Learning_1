from selenium import webdriver
from AOS_Automation.POM_main_page import Main_Page
from AOS_Automation.Ecxel_prog import Excel_AOS
from AOS_Automation.POM_category_page import Category_Page
from AOS_Automation.POM_product_page import Product_Page
import time
exel=Excel_AOS()
driver =webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')
main_page=Main_Page(driver)
cat_page=Category_Page(driver)
prod_page=Product_Page(driver)
driver.implicitly_wait(20)
driver.get('https://www.advantageonlineshopping.com/#/')
#
#
main_page.open_category_page_product(exel.product_1('category',6))
cat_page.open_product_page(exel.product_1('id',6))
prod_page.add_product_quantity(exel.product_1('quantity',6))
prod_page.click_add_to_cart_btn()
prod_page.open_main_page()
time.sleep(1)
main_page.open_category_page_product(exel.product_2('category',6))
time.sleep(1)
cat_page.open_product_page(exel.product_2('id',6))
time.sleep(1)
prod_page.add_product_quantity(exel.product_2('quantity',6))
prod_page.click_add_to_cart_btn()
prod_page.open_cart_page()








