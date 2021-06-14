from selenium import webdriver
import time

browser_drive = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')

browser_drive.implicitly_wait(10)
browser_drive.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

pop_up_close = browser_drive.find_element_by_id('at-cv-lightbox-close')
pop_up_close.click()

element_1 = browser_drive.find_element_by_id('user-message')  # חיפןש לפי ID לא תמיד קיימת אופציה כזו

element_1.send_keys("Hello world")

show_message=browser_drive.find_element_by_css_selector('button[onclick="showInput();"]')
show_message.click()

enter_1_element=browser_drive.find_element_by_id('sum1')
enter_1_element.send_keys(10)
enter_2_element=browser_drive.find_element_by_id('sum2')
enter_2_element.send_keys(20)
total_button = browser_drive.find_element_by_css_selector('button[onclick="return total()"]')
total_button.click()
num_1=browser_drive.find_element_by_id('displayvalue').text
input_0 = browser_drive.find_element_by_id('sum1').get_attribute("value")
input_1 = browser_drive.find_element_by_id('sum2').get_attribute("value")
sum_1=int(input_1)+int(input_0)
time.sleep(2)
if int(num_1)==int(sum_1) and int(num_1)==30:
    print('passed')
else:
    print('Not passed')

browser_drive.close()
