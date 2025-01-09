import time

def wait_for_element(page, selector, timeout=20):
    """
    Ожидание элемента по селектору с таймаутом.
    :param page: Объект страницы Playwright
    :param selector: селектор для поиска элемента
    :param timeout: максимальное время ожидания в секундах
    """
    for _ in range(timeout):
        try:
            if page.locator(selector).is_visible():
                print("Элемент найден!")
                break
            else:
                print(f"Element {selector} not found, still wait...")
        except Exception as e:
            print(f"Ошибка: {e}")
        time.sleep(1)
    else:
        print("Error! Element not found.")

