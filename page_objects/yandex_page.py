from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class YandexSearchPage():
    delay = 2

    search_box_locator = (By.ID, 'text')
    suggest_box_locator = (By.CLASS_NAME, 'mini-suggest__popup-content')
    request_results_locator = (By.CSS_SELECTOR, "li.serp-item")

    def __init__(self, driver):
        self.driver = driver

    def find_search_box(self):
        search_box = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(self.search_box_locator))
        return search_box

    def set_text_to_search_box(self, text_for_search: str):
        search_box = self.find_search_box()
        search_box.send_keys(text_for_search)

    def send_enter_to_search_box(self):
        search_box = self.find_search_box()
        search_box.send_keys(Keys.RETURN)

    def find_suggest_box(self):
        suggest_box = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(self.suggest_box_locator))
        return suggest_box

    def get_request_results(self):
        WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(self.request_results_locator))
        request_results = self.driver.find_elements_by_css_selector(self.request_results_locator[1])
        return request_results
