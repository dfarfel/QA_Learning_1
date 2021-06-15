from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


browser=webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')
browser.implicitly_wait(15)
browser.get('https://vk.com/')

email=browser.find_element_by_id('index_email')
email.send_keys('dfarfel05@gmail.com')

password=browser.find_element_by_id('index_pass')
password.send_keys('hervsem99')

browser.find_element_by_id('index_login_button').click()

browser.find_element_by_css_selector('a[class="left_row"][href="/im"]').click()

browser.switch_to.frame()

browser.get('https://vk.com/im?sel=101083645')
for i in range (40):
    try:
        send_message=browser.find_element_by_css_selector("[id='im_editable101083645']")

        send_message.send_keys(f'Hello world {i}')

        browser.find_element_by_css_selector('[class="im-send-btn im-chat-input--send _im_send im-send-btn_send"]').click()


    except:
        try:
            time.sleep(5)
            browser.refresh()
            error_element=browser.find_element_by_css_selector('[class="im-mess--marker _im_mess_marker"][aria-label="Ошибка при отправке сообщения"]')
            mouse=ActionChains(browser)
            mouse.click(on_element=error_element).perform()
            browser.find_element_by_xpath(
                '//a[@class="im-settings--item ui_actions_menu_item _im_failed_action"][@data-action="resend_all"]')
            browser.find_element_by_css_selector(
                '[class="im-send-btn im-chat-input--send _im_send im-send-btn_send"]').click()
        except:
            time.sleep(5)
            browser.refresh()
            error_element = browser.find_element_by_css_selector(
                '[class="im-mess--marker _im_mess_marker"][aria-label="Ошибка при отправке сообщения"]')
            mouse = ActionChains(browser)
            mouse.move_to_element(to_element=error_element).perform()
            browser.find_element_by_xpath(
                '//a[@class="im-settings--item ui_actions_menu_item _im_failed_action"][@data-action="resend_all"]')
            browser.find_element_by_css_selector(
                '[class="im-send-btn im-chat-input--send _im_send im-send-btn_send"]').click()



