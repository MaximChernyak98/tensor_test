import pytest
import os
import time
from selenium import webdriver
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from page_objects.yandex_search_page import YandexSearchPage
from page_objects.yandex_pictures_page import YandexPicturesPage


class Test_002_Pictures:
    logger = LogGen.loggen()

    logger.info("Test_002_Pictures")
    path_to_screenshots = os.path.join('.', 'screenshots')
    # TODO добавить скриншоты

    yandex_search_URL = ReadConfig.get_yandex_search_url()
    yandex_pictures_URL = ReadConfig.get_yandex_pictures_url()

    def test_yandex_pictures_section_exist(self, setup):
        self.logger.info("Checking if a Pictures section exists")
        self.driver = setup
        self.driver.get(self.yandex_search_URL)
        self.yp = YandexSearchPage(self.driver)
        try:
            self.yp.find_yandex_pictures_section()
            self.logger.info(f"Test passed: Pictures section found by {self.yp.pictures_section_locator}")
        except TimeoutException:
            self.logger.error(f"Test failed: Pictures section not found by {self.yp.pictures_section_locator} for {self.yp.delay} seconds")
        finally:
            self.driver.quit()
            self.logger.info("---------------")

    def test_yandex_pictures_page_exist(self, setup):
        self.logger.info("Checking yandex pictures page exist")
        self.driver = setup
        self.driver.get(self.yandex_search_URL)
        self.yp = YandexSearchPage(self.driver)
        try:
            pictures_section = self.yp.find_yandex_pictures_section()
            pictures_section.click()
            self.yp.find_yandex_pictures_title()
            self.logger.info(f"Test passed: successful transition to the https://yandex.ru/images/")
        except TimeoutException:
            self.logger.error(f"Test failed: can't find picture title by {self.yp.pictures_title_locator} for {self.yp.delay} seconds")
            assert False
        finally:
            self.driver.quit()
            self.logger.info("---------------")

    def test_yandex_pictures_first_category(self, setup):
        self.logger.info("Checking the correctness of image search")
        self.driver = setup
        self.driver.get(self.yandex_pictures_URL)
        self.yp = YandexPicturesPage(self.driver)
        try:
            first_popular_request = self.yp.find_first_popular_request()
            first_popular_request.click()
            expected_text = first_popular_request.text

            picture_search_box = self.yp.find_picture_search_box()
            actual_text = picture_search_box.get_attribute("value")
            if expected_text == actual_text:
                self.logger.info(f"Test passed: the text of the first category matches with the search text")
            else:
                self.logger.error(f"Test failed: the text of the first category does not match the search text")
        except TimeoutException:
            self.logger.error(f"Test failed: can't find element {self.yp.pictures_title_locator} for {self.yp.delay} seconds")
            assert False
        finally:
            self.driver.quit()
            self.logger.info("---------------")
