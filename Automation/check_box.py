from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')

browser.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')

checkbox_list=browser.find_elements_by_css_selector('[class="cb1-element"][type="checkbox"]')

checkbox_list[0].click()
checkbox_list[0].send_keys(Keys.PAGE_DOWN)