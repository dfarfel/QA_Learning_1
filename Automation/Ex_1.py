from selenium import webdriver
import time
message=input("Enter the message: ")

browser_drive = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe') #open the browser

browser_drive.implicitly_wait(10) #wait for element in browser

browser_drive.maximize_window()

browser_drive.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html') # Open the site

element_2=browser_drive.find_element_by_css_selector('#at-cv-lightbox-close')#Create element
element_2.click()#Click on element
element_1 = browser_drive.find_element_by_css_selector('#get-input > div:nth-child(1) > input:nth-child(2)')
element_1.send_keys("Hello world")#Send keys to element(Writing)
time.sleep(1)
element_1.clear()#
time.sleep(1)
element_1.send_keys(message)
time.sleep(1)
element3=browser_drive.find_element_by_css_selector('#get-input > button')
element3.click()
element4 = browser_drive.find_element_by_css_selector('#display')
text_1=element4.text
if text_1==message:
    print("passed")
browser_drive.close()

