from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
import pytest
import platform


def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome')


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def browser_with_options(browser):
    if browser == 'firefox':
        browser_options = webdriver.FirefoxOptions()
    elif browser == 'edge':
        browser_options = EdgeOptions()
    else:
        browser_options = webdriver.ChromeOptions()

    if browser == 'edge':
        browser_options.use_chromium = True
        # browser_options.add_argument("no-sandbox")
        browser_options.add_argument("window-size=1420,1080")
        browser_options.add_argument("headless")
        browser_options.add_argument("disable-gpu")
    else:
        browser_options.add_argument('--no-sandbox')
        browser_options.add_argument('--window-size=1420,1080')
        browser_options.add_argument('--headless')
        browser_options.add_argument('--disable-gpu')

    if browser == 'firefox':
        driver = webdriver.Firefox(firefox_options=browser_options)
    elif browser == 'edge':
        driver = Edge(options=browser_options)
    else:
        driver = webdriver.Chrome(chrome_options=browser_options)


@pytest.fixture()
def setup(browser):
    driver = None
    if platform.system() == 'Windows':
        if browser == 'firefox':
            driver = webdriver.Firefox()
            print("Launching Firefox Browser")
        elif browser == 'edge':
            driver = webdriver.Edge()
            print("Launching Edge Browser")
        else:
            driver = webdriver.Chrome()
            print("Launching Chrome Browser")
    else:
        driver = browser_with_options(browser)
    return driver

# PyTest HTML-report


def pytest_configure(config):
    config._metadata['Project Name'] = 'test project'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Mecher'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('1', None)
    metadata.pop('2', None)
