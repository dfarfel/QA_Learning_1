from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

    customer_type=browser.find_element_by_id('selusertype')
    select_type=Select(customer_type)
    select_type.select_by_value('guest')

    first_name=browser.find_element_by_id('fname')
    first_name.send_keys('Tester')

    last_name=browser.find_element_by_id('lname')
    last_name.send_keys("Tester1")

    phone=browser.find_element_by_id('mobile')
    phone.send_keys("0541233967")

    email=browser.find_element_by_id('email')
    email.send_keys('aba@mail.com')

    browser.find_element_by_css_selector('input[id="Tours"]').click()
    email.send_keys(Keys.PAGE_DOWN)
    for i in range (4):
        browser.find_element_by_xpath('//table[@class=" table-condensed"]/thead/tr/th[@class="next"]').click()
    date_table=browser.find_element_by_css_selector('[class=" table-condensed"]')
    date_rows=date_table.find_elements_by_tag_name("tr")
    for date_row in date_rows:
        cells_in_row=date_row.find_elements_by_css_selector('td')
        for cell in cells_in_row:
            if cell.text=="28":
                cell_1=cell
                break
    cell_1.click()
    email.click()

    tour_name=browser.find_element_by_css_selector('[id="s2id_autogen3"]>a>[class="select2-chosen"]')
    tour_name.click()
    browser.find_element_by_xpath('//div[@id="select2-drop"]/ul[@class="select2-results"]/li[3]').click()

    adults=browser.find_element_by_id('adults')
    select_adults=Select(adults)
    select_adults.select_by_index(2)

    child=browser.find_element_by_id('children')
    select_child=Select(child)
    select_child.select_by_index(1)



    payment=browser.find_element_by_name('paymethod')
    select_payment=Select(payment)
    select_payment.select_by_value('paypal')

    extras_9=browser.find_element_by_id('extras_9')
    mouse=ActionChains(browser)
    mouse.move_to_element(to_element=extras_9).perform()
    mouse.click(on_element=extras_9).perform()


    browser.find_element_by_css_selector('input[class="btn btn-primary btn-lg"]').click()
    list_option_1=browser.find_elements_by_css_selector('[class="btn btn-success"]')[1].click()
    #
    #
    # # browser.close()
