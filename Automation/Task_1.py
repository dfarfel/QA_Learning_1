from selenium import webdriver
import time
for i in range (2):
    browser =webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')
    browser.implicitly_wait(20)
    browser.get('https://www.phptravels.net/admin')
    browser.maximize_window()

    input_email=browser.find_element_by_css_selector('input[name="email"][placeholder="Email"]')
    input_email.send_keys('admin@phptravels.com')
    #time.sleep(1)

    input_password=browser.find_element_by_name('password')
    input_password.click()
    input_password.send_keys("demoadmin")
    #time.sleep(1)

    login_button=browser.find_element_by_css_selector('button[data-wow-duration="2s"]')
    login_button.click()

    dashboard_element=browser.find_element_by_css_selector('a[href="https://www.phptravels.net/admin"]')
    text_1=dashboard_element.text
    if text_1=="DASHBOARD":
        print ('Success')
    else :
        print ('Not passed')

    quik_button=browser.find_element_by_css_selector('button[data-toggle="modal"]')
    quik_button.click()
    select_tours=browser.find_element_by_css_selector('select[id="servicetype"]')
    select_tours.click()
    select_tours_1=browser.find_element_by_css_selector('option[value="Tours"]')
    select_tours_1.click()

    next_button=browser.find_element_by_css_selector('button[class="btn btn-primary"]')
    next_button.click()


    browser.close()