import pytest
import os
import time
from selenium import webdriver
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from page_objects.yandex_search_page import YandexSearchPage


class Test_002_Pictures:
    logger = LogGen.loggen()

    logger.info("Test_002_Pictures")
    path_to_screenshots = os.path.join('.', 'screenshots')
    # TODO добавить скриншоты

    yandexURL = ReadConfig.get_application_url()

    def test_check_search_box(self, setup):
        self.logger.info("Checking if a Pictures section exists")
        self.driver = setup
        self.driver.get(self.yandexURL)
        self.yp = YandexSearchPage(self.driver)
        try:
            self.yp.find_yandex_pictures_section()
            self.logger.info(f"Test passed: Pictures section found by {self.yp.pictures_section_locator}")
        except TimeoutException:
            self.logger.error(f"Test failed: Pictures section not found by {self.yp.pictures_section_locator} for {self.yp.delay} seconds")
        finally:
            self.driver.close()
            self.logger.info("---------------------------------------")

    @pytest.mark.current
    def test_suggests_in_search_box(self, setup):
        self.logger.info("Checking suggests in search field")
        self.driver = setup
        self.driver.get(self.yandexURL)
        self.yp = YandexSearchPage(self.driver)
        try:
            pictures_section = self.yp.find_yandex_pictures_section()
            pictures_section.click()
            self.yp.find_yandex_pictures_title()

            # self.yp.send_enter_to_search_box()
            # request_results = self.yp.get_request_results()
            # if request_results:
            #     self.search_href_in_list_of_links(request_results=request_results,
            #                                       link_to_search=r"https://tensor.ru/",
            #                                       number_results=5)
            # else:
            #     self.logger.error("Test failed: There is no links in result of search")
        except TimeoutException:
            pass
            # TODO добавить отработку различных ненайденок
            #self.logger.error(f"Test failed: Suggest field not found by {self.yp.suggest_box_locator} for {self.yp.delay} seconds")
        finally:
            self.driver.close()
            self.logger.info("---------------------------------------")
