from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

for i in range(1):
    browser = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')  # חיבור לדראייבר
    browser.implicitly_wait(20)  # המתנה לתגובה במקרה ואתר עולה לאט
    browser.get('https://www.phptravels.net/admin')  # פתיחת אתר לפי URL
    browser.maximize_window()  # הגדלת חלון

    input_email = browser.find_element_by_css_selector('input[name="email"][placeholder="Email"]')  # חיפוש לפי CSS
    input_email.send_keys('admin@phptravels.com')  # שליחת מפתחות(נתונים)
    # time.sleep(1)

    input_password = browser.find_element_by_name('password')
    input_password.click()
    input_password.send_keys("demoadmin")
    # time.sleep(1)

    login_button = browser.find_element_by_css_selector('button[data-wow-duration="2s"]')
    login_button.click()

    dashboard_element = browser.find_element_by_css_selector('ul[id="social-sidebar-menu"]>li>a>strong')
    text_1 = dashboard_element.text
    if text_1 == "DASHBOARD":
        print('Success')
    else:
        print('Not passed')

    quik_button = browser.find_element_by_css_selector('button[data-toggle="modal"]')
    quik_button.click()
    tours = browser.find_element_by_css_selector('#servicetype')
    tours.click()
    select_tours=Select(tours)
    select_tours.select_by_visible_text("Tours")

    next_button = browser.find_element_by_css_selector('button[class="btn btn-primary"]')
    next_button.click()

    browser.close()
