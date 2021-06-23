from selenium import webdriver
from AOS_Automation.POM_main_page import Main_Page
from AOS_Automation.Ecxel_prog import Excel_AOS
from AOS_Automation.POM_category_page import Category_Page
from AOS_Automation.POM_product_page import Product_Page
from AOS_Automation.POM_cart_page import Cart_Page
from AOS_Automation.POM_Payment_Page import Payment_Page
from AOS_Automation.POM_Create_Account import Create_Account_Page
from selenium.webdriver.common.action_chains import ActionChains
from AOS_Automation.POM_Orders_Page import Orders_Page
import time

exel = Excel_AOS()
driver = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')
payment_page = Payment_Page(driver)
mouse = ActionChains(driver)
main_page = Main_Page(driver)
order_page=Orders_Page(driver)
categ_page = Category_Page(driver)
create_account = Create_Account_Page(driver)
prod_page = Product_Page(driver)
cart_page = Cart_Page(driver)
driver.implicitly_wait(20)
driver.get('https://www.advantageonlineshopping.com/#/')
















# main_page.open_category_page('laptops')
# categ_page.open_product_page('7')
# prod_page.click_add_to_cart_btn()
# prod_page.click_checkout_btn()
# payment_page.open_registration_page()
# create_account.type_new_password(exel.new_account('password', 8))
# create_account.type_new_email(exel.new_account('email', 8))
# create_account.type_new_username(exel.new_account('username', 8))
# create_account.click_element_btn()
# create_account.click_registration_btn()
# payment_page.click_next_btn()
# payment_page.type_savepay_username(exel.new_account('username', 8))
# payment_page.type_savepay_password(exel.new_account('password', 8))
# payment_page.click_pay_now_btn()
# thank=payment_page.thank_you_element_txt()
# if 'Thank' in thank:
#     print("Order was successfully done")
# else:
#     print('Error in identification of order')
# order_number = payment_page.order_number_element_txt()
# prod_page.open_cart_page()
# empty=cart_page.cart_is_empty_element_txt()
# if 'empty' in empty:
#     print('Cart is empty OK')
# else:
#     print('Error with cart empty element')
#
# prod_page.open_my_orders()
# order_number_1=order_page.order_number(1)
# list_1=[]
# for object in order_number_1:
#     object_1=object.text
#     list_1.append(object_1)
# print(list_1)
# if order_number_1==order_number:
#     print("Succes")
#     print('wtf')
#
# else:
#     print(order_number_1)
#     print(order_number)
#     print("Fuck")