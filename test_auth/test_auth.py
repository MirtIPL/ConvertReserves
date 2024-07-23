import re
from playwright.sync_api import Page, expect


def test_auth_admin(page: Page) -> None:
    page.goto("https://dev-converter.sgp72.ru/")
    page.get_by_role("button", name="Авторизация").click()
    page.get_by_label("Почта").click()
    page.get_by_label("Пароль").click()
    page.get_by_text("Запомнить меня").click()
    page.get_by_label("Почта").click()
    page.get_by_label("Почта").click()
    page.get_by_label("Почта").fill("Admin@mail.com")
    page.get_by_label("Почта").press("Tab")
    page.get_by_label("Пароль").click()
    page.get_by_label("Пароль").fill("Test1234.")
    page.get_by_role("main").get_by_role("button", name="Войти").click()
    page.goto("https://dev-converter.sgp72.ru/projects")
    #expect(page.get_by_role("heading", name="Мои проекты")).to_be_visible()

def test_auth_expert(page: Page) -> None:
    page.goto("https://dev-converter.sgp72.ru/")
    page.get_by_role("button", name="Авторизация").click()
    page.get_by_label("Почта").click()
    page.get_by_label("Пароль").click()
    page.get_by_text("Запомнить меня").click()
    page.get_by_label("Почта").click()
    page.get_by_label("Почта").click()
    page.get_by_label("Почта").fill("Expert@mail.com")
    page.get_by_label("Почта").press("Tab")
    page.get_by_label("Пароль").click()
    page.get_by_label("Пароль").fill("Test1234.")
    page.get_by_role("main").get_by_role("button", name="Войти").click()
    page.goto("https://dev-converter.sgp72.ru/projects")
    #expect(page.get_by_role("heading", name="Мои проекты")).to_be_visible()

def test_auth_guset(page: Page) -> None:
    page.goto("https://dev-converter.sgp72.ru/")
    page.get_by_role("button", name="Авторизация").click()
    page.get_by_label("Почта").click()
    page.get_by_label("Пароль").click()
    page.get_by_text("Запомнить меня").click()
    page.get_by_label("Почта").click()
    page.get_by_label("Почта").click()
    page.get_by_label("Почта").fill("Guest@mail.com")
    page.get_by_label("Почта").press("Tab")
    page.get_by_label("Пароль").click()
    page.get_by_label("Пароль").fill("Test1234.")
    page.get_by_role("main").get_by_role("button", name="Войти").click()
    page.goto("https://dev-converter.sgp72.ru/projects")
    assert page.get_by_label("Пароль").is_hidden()


#Просмотр страницы Главная, автотесты



def test_vive_pkz(page: Page) -> None:
    page.goto("https://dev-converter.sgp72.ru/")
    page.get_by_role("button", name="Войти").click()
    page.get_by_label("Почта").click()
    page.get_by_label("Почта").fill("Admin@mail.com")
    page.get_by_label("Пароль").click(click_count=3)
    page.get_by_label("Пароль").fill("Test1234.")
    page.get_by_role("main").get_by_role("button", name="Войти").click()
    page.get_by_role("button", name="РКЗ").click()
    page.get_by_role("button", name="PRMS").click()
    page.get_by_role("button", name="РКООН").click()
    page.get_by_text("Сначала новые").click()
    expect(page.locator("#root")).to_contain_text("РКЗ")

def test_vive_pkooh(page: Page) -> None:
    page.goto("https://dev-converter.sgp72.ru/")
    page.get_by_role("button", name="Войти").click()
    page.get_by_label("Почта").click()
    page.get_by_label("Почта").fill("Admin@mail.com")
    page.get_by_label("Пароль").click(click_count=3)
    page.get_by_label("Пароль").fill("Test1234.")
    page.get_by_role("main").get_by_role("button", name="Войти").click()
    page.get_by_role("button", name="РКЗ").click()
    page.get_by_role("button", name="PRMS").click()
    page.get_by_role("button", name="РКООН").click()
    page.get_by_text("Сначала новые").click()
    expect(page.locator("#root")).to_contain_text("РКЗ")

def test_vive_prms(page: Page) -> None:
    page.goto("https://dev-converter.sgp72.ru/")
    page.get_by_role("button", name="Войти").click()
    page.get_by_label("Почта").click()
    page.get_by_label("Почта").fill("Admin@mail.com")
    page.get_by_label("Пароль").click(click_count=3)
    page.get_by_label("Пароль").fill("Test1234.")
    page.get_by_role("main").get_by_role("button", name="Войти").click()
    page.get_by_role("button", name="РКЗ").click()
    page.get_by_role("button", name="PRMS").click()
    page.get_by_role("button", name="РКООН").click()
    page.get_by_text("Сначала новые").click()
    expect(page.locator("#root")).to_contain_text("PRMS")

def test_vive_pkz_admin(page: Page) -> None:
    page.goto("https://dev-converter.sgp72.ru/")
    page.get_by_role("button", name="Войти").click()
    page.get_by_label("Почта").click()
    page.get_by_label("Почта").fill("Admin@mail.com")
    page.get_by_label("Пароль").click(click_count=3)
    page.get_by_label("Пароль").fill("Test1234.")
    page.get_by_role("main").get_by_role("button", name="Войти").click()
    page.get_by_role("button", name="РКЗ").click()
    page.get_by_role("button", name="PRMS").click()
    page.get_by_role("button", name="РКООН").click()
    page.get_by_text("Сначала новые").click()
    expect(page.locator("#root")).to_contain_text("РКООН")

#