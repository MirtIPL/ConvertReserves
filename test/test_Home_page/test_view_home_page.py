import time

from utils.custom_wait import wait_for_element

import allure
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

from config import *
from test.test_Home_page.home_page_expect import *
from core.BaseTest import *


@pytest.mark.test_all_test
@pytest.mark.test_main_page
@allure.title("Переименование проекта")
@allure.description("Переименование проекта")
@allure.severity(allure.severity_level.CRITICAL)
def test_rename_project(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    # Авторизация
    authorization(page)
    # Создание проекта
    create_project_PRMS(page)
    # Переименование проекта
    # Переход на страницу мои проекты
    go_to_main_page(page)
    # Закрытие контекста и браузера
    del_project(page)

    context.close()
    browser.close()


@pytest.mark.test_all_test
@pytest.mark.test_main_page
@allure.title("Просмотр страницы: Мои проекты")
@allure.description("Просмотр страницы: Мои проекты")
@allure.severity(allure.severity_level.CRITICAL)
def test_display_home_page(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)

    # Авторизация
    authorization(page)
    # Проверка отображения домашней страницы
    expect_view_home_page(page)
    # Проверка меню управления проекта
    expect_main_project_memu(page)

    # Закрытие контекста и браузера
    context.close()
    browser.close()
