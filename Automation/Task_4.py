from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')
browser.implicitly_wait(15)
browser.maximize_window()
browser.get('http://demo.guru99.com/test/newtours/')

time.sleep(1)
UserName = browser.find_element_by_name('userName')
UserName.send_keys("tutorial")
tex='sdsa'
tex.isnumeric()
time.sleep(1)
UserPassword = browser.find_element_by_name('password')
UserPassword.send_keys('tutorial')

time.sleep(1)
submit = browser.find_element_by_name('submit')
submit.click()

time.sleep(1)
flight_button = browser.find_element_by_css_selector('a[href="reservation.php"]')
flight_button.click()

time.sleep(1)
one_way = browser.find_element_by_css_selector('input[value="oneway"]')
one_way.click()

time.sleep(1)
first = browser.find_element_by_css_selector('input[value="First"]')
first.click()

time.sleep(1)
continue_button = browser.find_element_by_name('findFlights')
continue_button.click()

time.sleep(2)
browser.close()
