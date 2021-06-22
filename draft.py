from selenium import webdriver
from AOS_Automation.POM_main_page import Main_Page
from AOS_Automation.Ecxel_prog import Excel_AOS
from AOS_Automation.POM_category_page import Category_Page
from AOS_Automation.POM_product_page import Product_Page
from AOS_Automation.POM_cart_page import Cart_Page
import time

exel = Excel_AOS()
driver = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')
main_page = Main_Page(driver)
categ_page = Category_Page(driver)
prod_page = Product_Page(driver)
cart_page = Cart_Page(driver)
driver.implicitly_wait(20)
driver.get('https://www.advantageonlineshopping.com/#/')
main_page.open_category_page('tablets')


print(driver.current_url)


