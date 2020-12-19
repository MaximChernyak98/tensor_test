from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class YandexSearchPage():
    delay = 2

    search_box_locator = (By.ID, 'text')
    suggest_box_locator = (By.CLASS_NAME, 'mini-suggest__popup-content')
    request_results_locator = (By.CSS_SELECTOR, 'li.serp-item')
    pictures_section_locator = (By.CSS_SELECTOR, '[data-id="images"]')
    pictures_title_locator = (By.CSS_SELECTOR, '[type="application/opensearchdescription+xml"]')

    def __init__(self, driver):
        self.driver = driver

    # Search box methods
    def find_search_box(self):
        search_box = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(self.search_box_locator))
        return search_box

    def set_text_to_search_box(self, text_for_search: str):
        search_box = self.find_search_box()
        search_box.send_keys(text_for_search)

    def send_enter_to_search_box(self):
        search_box = self.find_search_box()
        search_box.send_keys(Keys.RETURN)

    # Suggest box methods
    def find_suggest_box(self):
        suggest_box = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(self.suggest_box_locator))
        return suggest_box

    # Request methods
    def get_request_results(self):
        WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(self.request_results_locator))
        request_results = self.driver.find_elements_by_css_selector(self.request_results_locator[1])
        return request_results

    # Pictures methods
    def find_yandex_pictures_section(self):
        pictures_section = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(self.pictures_section_locator))
        return pictures_section

    def find_yandex_pictures_title(self):
        pictures_title = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(self.pictures_title_locator))
        return pictures_title
