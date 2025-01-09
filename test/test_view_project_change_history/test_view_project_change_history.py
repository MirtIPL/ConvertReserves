import re
import Links
import time

from utils.custom_wait import wait_for_element
import allure
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from config import *
from core.BaseTest import *
from playwright.sync_api import Page, expect


@pytest.mark.test_all_test
@pytest.mark.test_history
def test_view_project_change_history(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    # Создать проект prms
    create_project_PRMS(page)
    # Перейти в модуль история проекта
    open_project_history(page)
    # Удалить тестовый проект
    del_project(page)
    expect(page.locator("#root")).to_contain_text("Все0")

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_history
def test_project_change_history_grouping_order_date(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    # Создать проект prms
    create_project_PRMS(page)
    # Перейти в модуль история проекта
    open_project_history(page)

    # Проверка группировки: Дата
    expect(page.locator("#root")).to_contain_text("История изменений")
    expect(page.get_by_text("Дата")).to_be_visible()
    expect(page.locator("thead")).to_contain_text("Дата")
    page.get_by_text("Дата", exact=True).click()
    expect(page.get_by_text("Порядок группировки: Дата")).to_be_visible()

    # Удалить тестовый проект
    del_project(page)
    expect(page.locator("#root")).to_contain_text("Все0")

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_history
def test_view_project_change_history_grouping_order_typ(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    # Создать проект prms
    create_project_PRMS(page)
    # Перейти в модуль история проекта
    open_project_history(page)

    # Проверка группировки: Тип изменений
    expect(page.locator("#root")).to_contain_text("Тип изменений")
    expect(page.get_by_text("Тип изменений")).to_be_visible()
    expect(page.locator("thead")).to_contain_text("Тип изменений")
    page.get_by_text("Тип изменений", exact=True).click()
    expect(page.get_by_text("Порядок группировки: Тип изменений")).to_be_visible()
    # Удалить тестовый проект
    del_project(page)
    expect(page.locator("#root")).to_contain_text("Все0")

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_history
def test_view_project_change_history_grouping_who_changed(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    # Создать проект prms
    create_project_PRMS(page)
    # Перейти в модуль история проекта
    open_project_history(page)

    # Проверка группировки: Тип изменений
    expect(page.locator("#root")).to_contain_text("Кем изменен")
    expect(page.get_by_text("Кем изменен")).to_be_visible()
    expect(page.locator("thead")).to_contain_text("Кем изменен")
    page.get_by_text("Кем изменен", exact=True).click()
    expect(page.get_by_text("Порядок группировки: Кем изменен")).to_be_visible()

    # Удалить тестовый проект
    del_project(page)
    expect(page.locator("#root")).to_contain_text("Все0")

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_history
def test_view_project_change_history_grouping_control(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    authorization(page)
    # Создать проект prms
    create_project_PRMS(page)
    # Перейти в модуль история проекта
    open_project_history(page)

    # Проверка группировки: Тип изменений

    # Удалить тестовый проект
    del_project(page)
    expect(page.locator("#root")).to_contain_text("Все0")

    context.close()
    browser.close()
