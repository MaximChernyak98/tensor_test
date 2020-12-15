import pytest
import os
import time
from selenium import webdriver
from page_objects.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities import excel_utils


class Test_002_DDT_Login:
    baseURL = ReadConfig.get_application_url()

    path_to_excel_data = os.path.join('.', 'test_data', 'login_data.xlsx')

    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("***Test_002_DDT_Login***")
        self.logger.info("***Verifying Login DDT test***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = excel_utils.get_row_count(self.path_to_excel_data, 'Лист1')
        print('Number of Rows i a Excel: ', self.rows)

        status_list = []

        for row in range(2, self.rows + 1):
            self.user = excel_utils.read_data(self.path_to_excel_data, 'Лист1', row, 1)
            self.password = excel_utils.read_data(self.path_to_excel_data, 'Лист1', row, 2)
            self.exp = excel_utils.read_data(self.path_to_excel_data, 'Лист1', row, 3)

            self.lp.set_user_name(self.user)
            self.lp.set_password(self.password)
            self.lp.click_login_button()
            time.sleep(2)

            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if actual_title == expected_title:
                if self.exp == 'Pass':
                    self.logger.info('*** Passed ***')
                    self.lp.click_logout_button()
                    status_list.append('Pass')
                elif self.exp == 'Fail':
                    self.logger.error('*** Failed ***')
                    self.lp.click_logout_button()
                    status_list.append('Fail')
            elif actual_title != expected_title:
                if self.exp == 'Pass':
                    self.logger.error('*** Failed ***')
                    status_list.append('Fail')
                elif self.exp == 'Fail':
                    self.logger.info('*** Passed ***')
                    status_list.append('Pass')

        if 'Fail' not in status_list:
            self.logger.info('*** Login DDT test is passed ***')
            self.driver.close()
            assert True
        else:
            self.logger.error('*** Login DDT test is failed ***')
            self.driver.close()
            assert False

        self.logger.info('*** End of Login DDT Test ***')
        self.logger.info('\n')
