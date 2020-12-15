import pytest
import os
import time
from selenium import webdriver
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from page_objects.yandex_page import YandexSearchPage


class Test_001_Search:
    logger = LogGen.loggen()
    # TODO сделать логгер в режиме добавления записей
    logger.info("Test_001_Search")
    path_to_screenshots = os.path.join('.', 'screenshots')
    # TODO добавить скриншоты

    yandexURL = ReadConfig.get_application_url()

    def test_check_search_box(self, setup):
        self.logger.info("Checking if a search field exists")
        self.driver = setup
        self.driver.get(self.yandexURL)
        self.yp = YandexSearchPage(self.driver)
        try:
            self.yp.find_search_box()
            self.logger.info(f"Test passed: Search field found by {self.yp.search_box_locator}")
        except TimeoutException:
            self.logger.error(f"Test failed: Search field not found by {self.yp.search_box_locator} for {self.yp.delay} seconds")
        finally:
            self.driver.close()

    @pytest.mark.current
    def test_suggests_in_search_box(self, setup):
        self.logger.info("Checking suggests in search field")
        self.driver = setup
        self.driver.get(self.yandexURL)
        self.yp = YandexSearchPage(self.driver)
        try:
            self.yp.set_text_to_search_box('Тензор')
            self.yp.find_suggest_box()
            self.yp.send_enter_to_search_box()
            request_results = self.yp.get_request_results()
            if request_results:
                self.search_href_in_list_of_links(request_results=request_results,
                                                  link_to_search=r"https://tensor.ru/",
                                                  number_results=5)
            else:
                self.logger.error("Test failed: There is no links in result of search")
        except TimeoutException:
            # TODO добавить отработку различных ненайденок
            self.logger.error(f"Test failed: Suggest field not found by {self.yp.suggest_box_locator} for {self.yp.delay} seconds")
        finally:
            self.driver.close()

    def search_href_in_list_of_links(self, request_results, link_to_search: str, number_results: int):
        list_of_links = []
        for element in request_results:
            element_with_link = element.find_element_by_tag_name('a')
            link = element_with_link.get_attribute("href")
            list_of_links.append(link)

        if link_to_search in list_of_links:
            index = list_of_links.index(link_to_search) + 1
            if index <= number_results:
                self.logger.info(f"Test passed: {link_to_search} find in {index} request position")
            else:
                self.logger.error(f"Test failed: {link_to_search} find, but in {index} request position")
        else:
            self.logger.error(f"Test failed: {link_to_search} did not find in request")
