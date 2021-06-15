from Automation_POM_Task_4.Task_4_POM_Main_page import main_page
from Automation_POM_Task_4.Task_4_POM_Login_page import guru_login_page
from selenium import webdriver
from unittest import TestCase


class Test_Task_4(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')
        self.driver.get('http://demo.guru99.com/test/newtours/')
        self.driver.implicitly_wait(10)

    def test_login(self):
        login_page = guru_login_page(self.driver)
        login_page.type_username()
        login_page.type_password()
        login_page.submit_btn_click()
        main_page_1 = main_page(self.driver)
        self.assertEqual(main_page_1.login_succes().text, 'Login Successfully')
