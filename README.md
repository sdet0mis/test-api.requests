# Проект тестирования API WordPress

## Развертывание проекта

`docker-compose up` - запускает Docker контейнеры, база данных MySQL и Apache сервер с предустановленным WordPress. Порты можно изменить при необходимости в docker-compose.yml.

По-умолчанию localhost:
- порт 8000 для доступа к wordpress
- порт 3306 для доступа к mysql

Подключение к базе данных:
- порт: 3306
- БД: wordpress
- user: wordpress
- password: wordpress

## Запуск тестов

Создать виртуальное окружение `python -m venv .venv`\
Активировать виртуальное окружение `source .venv/bin/activate`\
Установить зависимости `pip install -r requirements.txt`\
Запустить тесты `pytest --alluredir=allure-results`\
Открыть отчет `allure serve allure-results`
