
from selenium import webdriver

class Payment_Page:
    def __init__(self, driver):
        self.driver = driver
        #self.driver = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')

    def type_exists_username(self,username):
        self.driver.find_element_by_name('usernameInOrderPayment').send_keys(username)

    def type_exists_password(self,password):
        self.driver.find_element_by_name('passwordInOrderPayment').send_keys(password)

    def click_login_btn(self):
        self.driver.find_element_by_id('login_btnundefined').click()

    def click_next_btn(self):
        self.driver.find_element_by_id('next_btn').click()

    def open_registration_page(self):
        self.driver.find_element_by_id('registration_btnundefined').click()

    def type_savepay_username(self,username):
        self.driver.find_element_by_name('safepay_username').send_keys(username)

    def type_savepay_password(self,password):
        self.driver.find_element_by_name('safepay_password').send_keys(password)

    def click_pay_now_btn(self):
        self.driver.find_element_by_id('pay_now_btn_SAFEPAY').click()

    def thank_you_element(self):
        self.driver.find_element_by_css_selector('[id="orderPaymentSuccess"]>h2')

    def thank_you_element_txt(self):
        return self.driver.find_element_by_css_selector('[id="orderPaymentSuccess"]>h2').text

    def order_number_element(self):
        self.driver.find_element_by_id('orderNumberLabel')

    def order_number_element_txt(self):
        return self.driver.find_element_by_id('orderNumberLabel').text



