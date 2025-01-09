import json
import os

DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), "data.json")


def read_value(key):
    try:
        with open(DATA_FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data.get(key, None)
    except FileNotFoundError:
        print(f"Ошибка: файл {DATA_FILE_PATH} не найден.")
        return None
    except json.JSONDecodeError:
        print(f"Ошибка: файл {DATA_FILE_PATH} не является допустимым JSON.")
        return None


def write_value(key, value):
    try:
        with open(DATA_FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        data[key] = value

        with open(DATA_FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
    except FileNotFoundError:
        print(f"Ошибка: файл {DATA_FILE_PATH} не найден.")
    except json.JSONDecodeError:
        print(f"Ошибка: файл {DATA_FILE_PATH} не является допустимым JSON.")
