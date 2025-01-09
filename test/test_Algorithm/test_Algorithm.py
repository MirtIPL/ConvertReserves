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
def test_vive_algorithm_pks_pkooh(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)
    time.sleep(6)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_vive_algorithm_pkooh_pks(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_vive_algorithm_pkooh_prms(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_vive_algorithm_prms_pkooh(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_vive_algorithm_prms_pkooh_filter(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_vive_algorithm_filter_filter_category(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_vive_algorithm_filter_filter_proxy(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_vive_algorithm_filter_filter_type(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_vive_algorithm_filter_filter_start_of_production(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_vive_algorithm_filter_filter_fossil_use(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_vive_algorithm_filter_project_for(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_vive_algorithm_filter_viability(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_vive_algorithm_filter_accumulation(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_vive_algorithm_approved_project_document(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_vive_algorithm_filter_filter_fossil_use(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_vive_algorithm_filter_class(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_vive_algorithm_filter_subclass(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_vive_algorithm_filter_G(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_vive_algorithm_filter_E(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_vive_algorithm_filter_F(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all23
def test_vive_algorithm_filter_search(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_vive_algorithm_filter_сleaning_the_filter(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_algorithm_add_algorithm(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_algorithm_del_algorithm(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_algorithm_tree(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    ####Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_all5
def test_algorithm_tree_zoom(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)

    authorization(page)
    #Продолжить отсюда
    open_algoritm(page)

    context.close()
    browser.close()
