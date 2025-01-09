import re
import Links
import time

from playwright.sync_api import Page, expect
from utils.custom_wait import wait_for_element
import allure
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from config import *
from core.BaseTest import *


@pytest.mark.test_all
@pytest.mark.test_auth1
def test_auth_admin(page: Page) -> None:
    page.goto(Links.Url_dev)
    expect(page.get_by_role("button", name="Авторизация")).to_be_visible()
    page.get_by_role("button", name="Авторизация").click()
    expect(page.get_by_text("Почта")).to_be_visible()
    expect(page.get_by_text("Пароль", exact=True)).to_be_visible()
    expect(page.get_by_role("button", name="Запросить доступ")).to_be_visible()
    expect(page.get_by_role("button", name="Войти как Гость")).to_be_visible()
    expect(page.get_by_role("link", name="Забыли пароль?")).to_be_visible()
    page.get_by_label("Почта").click()
    page.get_by_label("Почта").fill("Admin@mail.com")
    page.get_by_label("Пароль").click()
    page.get_by_label("Пароль").fill("Test1234.")
    page.get_by_label("toggle password visibility").click()
    page.get_by_label("Запомнить меня").check()
    page.get_by_role("main").get_by_role("button", name="Войти", exact=True).click()
    expect(page.get_by_label("sign out")).to_be_visible()
    page.get_by_label("sign out").click()
    expect(page.get_by_role("button", name="Войти")).to_be_visible()


@pytest.mark.test_all
@pytest.mark.test_auth
def test_auth_vive(page: Page) -> None:
    page.goto(Links.Url_dev)
    page.get_by_role("button", name="Войти").click()
    expect(page.get_by_label("Почта")).to_be_visible()
    expect(page.get_by_label("Пароль")).to_be_visible()
    expect(page.get_by_role("main").get_by_role("button", name="Войти", exact=True)).to_be_visible()
    expect(page.get_by_role("button", name="Запросить доступ")).to_be_visible()
    expect(page.get_by_role("button", name="Войти как Гость")).to_be_visible()


@pytest.mark.test_all
@pytest.mark.test_auth
def test_Access_Request_test(page: Page) -> None:
    page.goto(Links.Url_dev)
    page.get_by_role("button", name="Войти").click()
    expect(page.get_by_label("Почта")).to_be_visible()
    expect(page.get_by_label("Пароль")).to_be_visible()
    expect(page.get_by_role("button", name="Запросить доступ")).to_be_visible()
    expect(page.get_by_role("button", name="Войти как Гость")).to_be_visible()
    expect(page.get_by_role("heading", name="Конвертер запасов")).to_be_visible()
    expect(page.locator("h1")).to_contain_text("Конвертер запасов")
    expect(page.get_by_role("button", name="Запросить доступ")).to_be_visible()
    page.get_by_role("button", name="Запросить доступ").click()
    expect(page.get_by_text(
        "Для получения доступа к Конвертеру запасов обратитесь к Администратору Системы")).to_be_visible()
    expect(page.get_by_text("Телефон:")).to_be_visible()
    expect(page.get_by_text("Почта:")).to_be_visible()
    page.get_by_role("button", name="Ок").click()
    expect(page.locator("form")).to_contain_text("Войти")


@pytest.mark.test_all
@pytest.mark.test_auth
def test_auth_invalid_login(page: Page) -> None:
    page.goto(Links.Url_dev)
    expect(page.get_by_role("button", name="Авторизация")).to_be_visible()
    page.get_by_role("button", name="Авторизация").click()
    expect(page.get_by_label("Почта")).to_be_visible()
    expect(page.get_by_label("Пароль")).to_be_visible()
    page.get_by_label("Почта").click()
    page.get_by_label("Почта").fill("Admin@mail")
    expect(page.get_by_label("Почта")).to_be_visible()
    page.get_by_label("Пароль").click()
    page.get_by_label("Пароль").fill("Test1234.")
    page.get_by_role("main").get_by_role("button", name="Войти", exact=True).click()
    expect(page.get_by_text("Неверный формат почты")).to_be_visible()
    expect(page.locator("#email-helper-text")).to_contain_text("Неверный формат почты")


@pytest.mark.test_all
@pytest.mark.test_auth
def test_auth_invalid_small_password(page: Page) -> None:
    page.goto(Links.Url_dev)
    page.get_by_role("button", name="Авторизация").click()
    page.get_by_label("Пароль").click()
    page.get_by_label("Пароль").fill("345")
    page.locator("div").filter(
        has_text="Конвертер запасовАвторизацияПочтаПарольЗапомнить меняЗабыли пароль?ВойтиИлиЗапро").nth(3).click()
    page.get_by_label("Пароль").click()
    page.get_by_label("Пароль").fill("34")
    page.get_by_role("main").get_by_role("button", name="Войти", exact=True).click()
    expect(page.get_by_text("Пароль слишком короткий")).to_be_visible()
    expect(page.locator("#password-helper-text")).to_contain_text("Пароль слишком короткий")
    expect(page.locator("#email-helper-text")).to_contain_text("Неверный формат почты")


@pytest.mark.test_all
@pytest.mark.test_auth
def test_auth_invalid_password(page: Page) -> None:
    page.goto(Links.Url_dev)
    page.get_by_role("button", name="Авторизация").click()
    page.get_by_label("Почта").fill("Admin@mail.com")
    page.get_by_label("Пароль").click()
    page.get_by_label("Пароль").fill("Test1234")
    page.get_by_role("main").get_by_role("button", name="Войти", exact=True).click()
    expect(page.get_by_role("paragraph")).to_be_visible()
    expect(page.get_by_role("paragraph")).to_contain_text("Неверный логин или пароль")


@pytest.mark.test_all
@pytest.mark.test_auth
def test_auth_login_as_guest(page: Page) -> None:
    page.goto(Links.Url_dev)
    page.get_by_role("button", name="Авторизация").click()
    page.locator("//*[@id='root']/div/div[2]/div/main/div[2]/button[2]").click()


@pytest.mark.test_all
@pytest.mark.test_auth
def test_auth_password_recovery(page: Page) -> None:
    page.goto(Links.Url_dev)
    page.get_by_role("button", name="Авторизация").click()
    expect(page.get_by_text("Почта")).to_be_visible()
    expect(page.get_by_text("Пароль", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="Забыли пароль?")).to_be_visible()
    page.get_by_role("link", name="Забыли пароль?").click()
    expect(page.get_by_text("Для восстановления пароля обратитесь к Администратору Системы")).to_be_visible()
    expect(page.get_by_role("dialog")).to_contain_text("Телефон:")


@pytest.mark.test_all
@pytest.mark.test_auth1
@allure.title("Тест")
@allure.description("Тест")
@allure.severity(allure.severity_level.CRITICAL)
def test_logout_page(playwright: Playwright) -> None:
    browser, context, page = setup_browser_and_context(playwright)
    # Авторизация
    authorization(page)
    # Выход из системы
    logout_page(page)

    context.close()
    browser.close()
