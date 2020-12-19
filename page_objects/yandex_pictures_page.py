from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class YandexPicturesPage():
    delay = 2

    first_popular_request_locator = (By.CSS_SELECTOR,
                                     '.PopularRequestList .ImagesList:nth-child(1) .PopularRequestList-Item:nth-child(1) .PopularRequestList-SearchText')
    picture_search_box_locator = (By.CSS_SELECTOR, '.serp-header__logo ~ .serp-header__search2 .input__control[name="text"]')

    def __init__(self, driver):
        self.driver = driver

    def find_first_popular_request(self):
        first_popular_request = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(self.first_popular_request_locator))
        return first_popular_request

    def find_picture_search_box(self):
        picture_search_box = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(self.picture_search_box_locator))
        return picture_search_box
