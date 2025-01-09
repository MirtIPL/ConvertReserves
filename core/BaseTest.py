import time

from utils.custom_wait import wait_for_element
import allure
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from config import *
from playwright.sync_api import Page, expect


def authorization(page):
    page.goto(BASE_URL)

    page.get_by_role("button", name="Авторизация").click()
    page.get_by_label("Почта").fill(USERNAME)
    page.get_by_label("Пароль").click()
    page.get_by_label("Пароль").fill(PASSWORD)
    page.get_by_role("main").get_by_role("button", name="Войти", exact=True).click()

    page.get_by_role("button", name="Войти").click()

    wait_for_element(page, "div/div[1]/h2")


def logout_page(page):
    expect(page.get_by_label("sign out")).to_be_visible()
    page.get_by_label("sign out").click()
    expect(page.get_by_role("button", name="Войти")).to_be_visible()


def open_algoritm(page):
    assert page.get_by_role("button", name="Справка").is_visible()
    page.get_by_role("button", name="Справка").click()
    # page.get_by_role("button", name="Справка").click()
    page.get_by_text("Алгоритмы").click()


def create_project_PRMS(page):
    page.get_by_role("button", name="Создать новый проект").click()
    page.get_by_label("edit project name").click()
    page.get_by_role("main").get_by_placeholder("Найти").press("ControlOrMeta+a")
    page.get_by_role("main").get_by_placeholder("Найти").fill(BASE_PROJECT_PRMS)
    page.get_by_role("main").get_by_placeholder("Найти").press("Enter")
    expect(page.locator("h2")).to_contain_text(BASE_PROJECT_PRMS)
    page.get_by_label("Without label").click()
    page.get_by_role("option", name="PRMS").click()
    page.get_by_role("button", name="Добавить").click()
    page.locator("input[name=\"Месторождение\"]").click()
    page.locator("input[name=\"Месторождение\"]").fill("1")
    page.get_by_role("option", name="1").click()
    page.locator("div:nth-child(2) > .MuiInputBase-root > .MuiSelect-select").click()
    page.get_by_role("option", name="Газовое", exact=True).click()
    page.locator("input[name=\"Группа эксплуатационных объектов\"]").click()
    page.locator("input[name=\"Группа эксплуатационных объектов\"]").fill("1")
    page.get_by_label("Close", exact=True).click()
    page.locator("input[name=\"Эксплуатационный объект\"]").click()
    page.locator("input[name=\"Эксплуатационный объект\"]").fill("1")
    page.get_by_role("option", name="1").click()
    page.locator("input[name=\"Пласт\"]").click()
    page.locator("input[name=\"Пласт\"]").fill("1")
    page.locator("input[name=\"Пласт\"]").press("Tab")
    page.locator("input[name=\"Залежь\"]").fill("1")
    page.locator("input[name=\"Залежь\"]").press("Tab")
    page.get_by_role("button", name="Дополнительные параметры").click()
    page.locator("input[name=\"Страна\"]").click()
    page.get_by_role("option", name="Куба").click()
    page.locator("input[name=\"Регион\"]").click()
    page.locator("input[name=\"Регион\"]").fill("44")
    page.get_by_role("option", name="44").click()
    page.locator("input[name=\"Собственник\"]").click()
    page.locator("input[name=\"Собственник\"]").fill("12")
    page.get_by_role("option", name="12").click()
    page.locator("#percentOwn").click()
    page.locator("#percentOwn").fill("12")
    page.locator(
        ".MuiAccordionDetails-root > div > div:nth-child(5) > .MuiAutocomplete-root > .MuiFormControl-root > .MuiInputBase-root").click()
    page.locator("input[name=\"Недропользователь\"]").fill("1")
    page.get_by_role("option", name="1").click()
    page.locator("input[name=\"Оператор\"]").click()
    page.locator("input[name=\"Оператор\"]").fill("12")
    page.get_by_role("option", name="12").click()
    page.locator("input[name=\"Лицензионный участок\"]").click()
    page.locator("input[name=\"Лицензионный участок\"]").fill("12")
    page.get_by_role("option", name="12").click()
    page.locator("input[name=\"Лицензионные обязательства \\/ ограничения\"]").click()
    page.locator("input[name=\"Лицензионные обязательства \\/ ограничения\"]").fill("12")
    page.get_by_role("option", name="12").click()
    page.locator("#yearOpen").click()
    page.locator("#yearOpen").fill("2000")
    page.locator("input[name=\"Метод подсчета\"]").click()
    page.get_by_role("option", name="Объемный", exact=True).click()
    page.locator("input[name=\"Организация\\, выполнившая оценку\"]").click()
    page.get_by_role("option", name="ВНИИГАЗ").click()
    page.locator("input[name=\"Отвественный исполнитель подсчета\"]").click()
    page.get_by_role("option", name="Отвественный исполнитель подсчета").click()
    page.locator("#countingData").fill("2019-10-16")
    page.get_by_role("button", name="Далее").click()
    page.locator("div:nth-child(2) > .MuiInputBase-root > .MuiSelect-select").first.click()
    page.get_by_text("Газовая шапка, млн.м").click()
    page.get_by_role("option", name="Газ свободный, млн.м").get_by_role("checkbox").check()
    page.get_by_role("option", name="Газ свободный, млн.м").press("Tab")
    page.locator(
        "#parametersForm > div > div:nth-child(2) > .MuiFormControl-root > .MuiInputBase-root > .MuiSelect-select").click()
    page.get_by_text("Низкая - C1").click()
    page.get_by_role("option", name="Возможные - P3").get_by_role("checkbox").check()
    page.get_by_role("option", name="Вероятные - P2").get_by_role("checkbox").check()
    page.get_by_role("option", name="Вероятные - P2").get_by_role("checkbox").press("Tab")
    page.locator("#productionStartYear").click()
    page.locator("#productionStartYear").fill("2000")
    page.get_by_text("Условные ресурсы").click()
    page.get_by_role("option", name="Запасы").click()
    page.locator("div:nth-child(5) > .MuiFormControl-root > .MuiInputBase-root > .MuiSelect-select").click()
    page.get_by_role("option", name="Разработка ожидается").click()
    page.get_by_text("Не определено").first.click()
    page.get_by_text("PDNP", exact=True).click()
    page.get_by_role("option", name="PDP").get_by_role("checkbox").check()
    page.get_by_role("option", name="PDP").get_by_role("checkbox").press("Tab")
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_role("button", name="Сохранить").dblclick()
    page.get_by_role("button", name="Сохранить").click(click_count=4)


def open_project_history(page):
    expect(page.get_by_role("complementary").locator("#basic-button")).to_be_visible()
    page.get_by_role("complementary").locator("#basic-button").click()
    expect(page.get_by_text("История изменений")).to_be_visible()
    page.get_by_text("История изменений").click()
    expect(page.locator("#root")).to_contain_text("История изменений")
    expect(page.get_by_role("listitem").first).to_be_visible()
    expect(page.get_by_label("Go to next page")).to_be_visible()
    expect(page.get_by_label("Отфильтровать по Дата")).to_be_visible()


def del_project(page):
    page.get_by_label("go home").click()
    page.get_by_placeholder("Найти").click()
    page.get_by_placeholder("Найти").fill(BASE_PROJECT_PRMS)
    page.get_by_placeholder("Найти").press("Enter")
    expect(page.locator("#root")).to_contain_text(BASE_PROJECT_PRMS)
    page.locator("#basic-button").nth(3).click()
    expect(page.get_by_label("Скачать шаблон")).to_contain_text("Удалить")
    page.get_by_text("Удалить").click()
    expect(page.get_by_role("dialog")).to_contain_text("Вы действительно хотите удалить?")
    page.get_by_role("button", name="Да").click()
    expect(page.locator("#root")).to_contain_text("Все0")



def del_copi_project(page):
    page.get_by_label("go home").click()
    page.get_by_placeholder("Найти").click()
    page.get_by_placeholder("Найти").press("ControlOrMeta+c")
    page.get_by_placeholder("Найти").fill(BASE_PROJECT_PRMS)
    page.get_by_placeholder("Найти").press("Enter")
    expect(page.locator("#root")).to_contain_text(BASE_PROJECT_PRMS)
    page.locator("#basic-button").nth(3).click()
    expect(page.get_by_label("Скачать шаблон")).to_contain_text("Удалить")
    page.get_by_text("Удалить").click()
    expect(page.get_by_role("dialog")).to_contain_text("Вы действительно хотите удалить?")
    page.get_by_role("button", name="Да").click()

    page.get_by_placeholder("Найти").click()
    page.get_by_placeholder("Найти").press("ControlOrMeta+c")
    page.get_by_placeholder("Найти").fill()
    page.get_by_placeholder("Найти").press("Enter")
    expect(page.locator("#root")).to_contain_text(BASE_PROJECT_COPI)
    page.locator("#basic-button").nth(3).click()
    expect(page.get_by_label("Скачать шаблон")).to_contain_text("Удалить")
    page.get_by_text("Удалить").click()
    expect(page.get_by_role("dialog")).to_contain_text("Вы действительно хотите удалить?")
    page.get_by_role("button", name="Да").click()
    expect(page.locator("#root")).to_contain_text("Все0")