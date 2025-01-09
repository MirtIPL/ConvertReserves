import re
import Links
import time

from utils.custom_wait import wait_for_element
import allure
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from config import BASE_URL, LOGIN_PAGE, USERNAME, PASSWORD, WAIT_TIME, setup_browser_and_context
from core.BaseTest import authorization, open_algoritm
from playwright.sync_api import Page, expect


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_test_conversion_result_view_rks(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)
    time.sleep(6)

    context.close()
    browser.close()
