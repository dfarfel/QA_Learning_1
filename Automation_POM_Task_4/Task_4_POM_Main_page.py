class main_page:
    def __init__(self, driver):
        self.driver = driver

    def login_succes(self):
        return self.driver.find_element_by_xpath("//*[text()='Login Successfully']")

    def flight_btn(self):
        return self.driver.find_element_by_css_selector('a[href="reservation.php"]')

    def flight_btn_click(self):
        self.flight_btn().click()

    def one_way_option_btn_click(self):
        self.driver.find_element_by_css_selector('input[value="oneway"]').click()

    def first_class_btn_click(self):
        self.driver.find_element_by_css_selector('input[value="First"]').click()

    def continue_btn(self):
        return self.driver.find_element_by_name('findFlights')

    def continue_btn_click(self):
        self.continue_btn().click()

    def back_to_home_btn(self):
        return self.driver.find_element_by_css_selector('[src="images/home.gif"]')
