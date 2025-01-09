# config.py
import allure
from time import sleep
import logging

import allure
from playwright.sync_api import expect

from playwright.sync_api import Playwright

BASE_URL = "https://dev-converter.sgp72.ru"
LOGIN_PAGE = ""
LOGIN_PARAMS = {
    "pid": "",
    "treePath": ""
}
USERNAME = "Admin@mail.com"
PASSWORD = "Test1234."
HEADLESS_MODE = False
IGNORE_HTTPS_ERRORS = True
WAIT_TIME = 2
BASE_PROJECT_COPI = "Копия TEST_1"
BASE_PROJECT_PRMS = "TEST_1"
expect.set_options(timeout=10_000)

def setup_browser_and_context(playwright: Playwright):
    browser = playwright.chromium.launch(
        headless=HEADLESS_MODE,
        args=["--start-maximized", "--force-device-scale-factor=0.75"]
    )

    context = browser.new_context(
        ignore_https_errors=IGNORE_HTTPS_ERRORS,
        no_viewport=True,
        accept_downloads=True,
        permissions=["clipboard-read", "clipboard-write"]
    )

    page = context.new_page()
    return browser, context, page


@allure.step('Проверить, что {expected_value} равно {actual_value}')
def check_values_equality(expected_value, actual_value):
    assert expected_value == actual_value


def get_text_by_element_span(locator):
    return locator.text_content()
