import pytest
import os
from selenium import webdriver
from page_objects.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    logger = LogGen.loggen()

    path_to_screenshots = os.path.join('.', 'screenshots')

    def test_home_page_title(self, setup):
        self.logger.info("***Test_001_Login***")
        self.logger.info("***Verifying Home Page Title***")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.logger.info("*** Home page title test is passed ***")
            self.driver.close()
        else:
            path_to_failed_home_page_title_test = os.path.join(self.path_to_screenshots,
                                                               'test_home_page_title_failed.png')
            self.driver.save_screenshot(path_to_failed_home_page_title_test)
            self.logger.error("*** Home page title test is failed ***")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger.info("***Verifying Login test***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_user_name(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login_button()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            self.logger.info("*** Login test is passed ***")
            self.driver.close()
            assert True
        else:
            path_to_failed_login_test = os.path.join(self.path_to_screenshots, 'test_login_failed.png')
            self.driver.save_screenshot(path_to_failed_login_test)
            self.logger.error("*** Login test is failed ***")
            self.driver.close()
            assert False
