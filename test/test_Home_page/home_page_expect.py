import time

from utils.custom_wait import wait_for_element

import allure
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

from config import *
from core.BaseTest import authorization


def expect_view_home_page(page):
    expect(page.locator("h2")).to_contain_text("Мои проекты")
    expect(page.get_by_role("button", name="Сформировать отчет")).to_be_visible()
    expect(page.get_by_role("button", name="Загрузить проект")).to_be_visible()
    expect(page.get_by_role("button", name="Создать новый проект")).to_be_visible()
    expect(page.get_by_text("Сначала новые")).to_be_visible()
    expect(page.locator("#tiles")).to_be_visible()
    expect(page.locator(".css-1wd1p7q-classificationContainer").first).to_be_visible()


def expect_main_project_memu(page):
    page.locator("#lists").click()
    page.locator("div:nth-child(4) > #basic-button").first.click()
    expect(page.get_by_label("Скачать шаблон")).to_contain_text("Переименовать")
    expect(page.get_by_role("menuitem", name="Сравнить")).to_be_visible()
    expect(page.get_by_text("Скачать", exact=True)).to_be_visible()
    expect(page.get_by_text("Дублировать")).to_be_visible()
    expect(page.get_by_text("Удалить")).to_be_visible()
    expect(page.get_by_label("Скачать шаблон")).to_contain_text("Сравнить")
    expect(page.get_by_label("Скачать шаблон")).to_contain_text("Скачать")
    expect(page.get_by_label("Скачать шаблон")).to_contain_text("Удалить")


def go_to_main_page(page):
    page.get_by_label("go home").click()
    page.get_by_placeholder("Найти").click()
    page.get_by_placeholder("Найти").fill(BASE_PROJECT_PRMS)
    page.get_by_placeholder("Найти").press("Enter")
    expect(page.locator("#root")).to_contain_text(BASE_PROJECT_PRMS)


def rename_project(page):
    page.get_by_role("main").get_by_placeholder("Найти").press("ControlOrMeta+a")
    page.get_by_role("main").get_by_placeholder("Найти").fill(BASE_PROJECT_PRMS)
    page.locator(".css-z3ce45-titleContainer > .MuiFormControl-root > .MuiInputBase-root").click()
    page.get_by_role("main").get_by_placeholder("Найти").press("Enter")
    expect(page.locator("h2")).to_contain_text(BASE_PROJECT_PRMS)
    expect(page.get_by_label("Without label")).to_contain_text("РКЗ")


def create_project_main_page(page):
    page.get_by_role("button", name="Создать новый проект").click()
    page.get_by_role("button", name="Добавить").click()
    page.get_by_label("close").click()
    page.get_by_label("edit project name").click()
