from selenium import webdriver
import time

browser_drive = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')

browser_drive.implicitly_wait(10)
browser_drive.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

pop_up_close = browser_drive.find_element_by_id('at-cv-lightbox-close')
pop_up_close.click()

element_1 = browser_drive.find_element_by_id('user-message')  # חיפןש לפי ID לא תמיד קיימת אופציה כזו

element_1.send_keys("Hello world")

time.sleep(5)

browser_drive.close()
