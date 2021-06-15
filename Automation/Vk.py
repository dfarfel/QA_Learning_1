from selenium import webdriver
import time

browser=webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')
browser.implicitly_wait(15)
browser.get('https://vk.com/')

email=browser.find_element_by_id('index_email')
email.send_keys('dfarfel05@gmail.com')

password=browser.find_element_by_id('index_pass')
password.send_keys('hervsem99')

browser.find_element_by_id('index_login_button').click()

browser.find_element_by_css_selector('a[class="left_row"][href="/im"]').click()

browser.get('https://vk.com/im?sel=101083645')
for i in range (40):
    send_message=browser.find_element_by_css_selector("[id='im_editable101083645']")

    send_message.send_keys("Hello world")

    browser.find_element_by_css_selector('[class="im-send-btn im-chat-input--send _im_send im-send-btn_send"]').click()

    time.sleep(2)


