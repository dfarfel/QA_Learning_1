
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

class Create_Account_Page:
    def __init__(self, driver):
        self.driver = driver
        #self.driver = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')

    def type_new_username(self,username):
        self.driver.find_element_by_name('usernameRegisterPage').send_keys(username)

    def type_new_password(self,password):
        self.driver.find_element_by_name('passwordRegisterPage').send_keys(password)
        self.driver.find_element_by_name('confirm_passwordRegisterPage').send_keys(password)

    def type_new_email(self,email):
        self.driver.find_element_by_name('emailRegisterPage').send_keys(email)

    def click_element_btn(self):
        self.driver.find_element_by_css_selector('[class="checkboxText roboto-light animated"]').click()

    def click_registration_btn(self):
        self.driver.find_element_by_id('register_btnundefined').click()