# new-Conv-tests


- `python - m venv venv` - Создать виртуальное окружение
- `venv\Scripts\activate` - Активировать вирутальное окружение Windows
- `source venv/bin/activate` - Активировать вирутальное окружение MacOS и Linux
- `python -m pip install --upgrade pip` - Обновить менеджер пакетов pip
- `pip install -r requirements.txt` - Установить все зависимости из файла requirements.txt
- `playwright install-deps` - Установить зависимости для Playwright
- `playwright install chromium` - Установить playwright (только Chromium)




### Запуск тестов в DEBUG режиме
Тесты можно запустить пошагово и с интерфейсом Playwright для дебага тестов используя флаг `PWDEBUG=1` в консоли.
Т.е. для того, чтобы запустить тест с маркером `test_pc_regress` 
необходимо выполнить команду: `PWDEBUG=1 -m test_pc_regress --headed`