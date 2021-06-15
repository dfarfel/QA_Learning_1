class guru_login_page:
    def __init__(self, driver):
        self.driver = driver

    def username(self):
        return self.driver.find_element_by_name('userName')

    def password(self):
        return self.driver.find_element_by_name('password')

    def type_password(self):
        self.password().send_keys('tutorial')

    def type_username(self):
        self.username().send_keys("tutorial")

    def submit_btn(self):
        return self.driver.find_element_by_name('submit')

    def submit_btn_click(self):
        self.submit_btn().click()
