# Тренировочный проект WordPress для автоматизации тестирования API и БД

## Общая информация
Для использования проекта нужен Docker и Docker-compose. 

Более подробно документацию к API WordPress можно получить на [офф сайте](http://v2.wp-api.org/)

После развертывания проекта для доступа к API WordPress можно воспользоваться ссылкой: 
[http://localhost:8000/index.php?rest_route=/](http://localhost:8000/index.php?rest_route=/)

Например получить список статей можно таким запросом:
[http://localhost:8000/index.php?rest_route=/wp/v2/posts](http://localhost:8000/index.php?rest_route=/wp/v2/posts)

## Инструкция по развертыванию проекта

 1. Установить docker - [ссылка на скачивание docker для Windows](https://www.docker.com/docker-windows)
 2. Распаковать архив и перейти в дирректорию скачанного проекта, где лежит docker-compose файл
 3. Открыть командную строку в дирректории из шага 3
 4. В командной строке выполнить команду – `docker-compose up`. 
Это приведёт к запуску двух контейнеров Docker, база данных MySQL и Apache сервер с предустановленным WordPress. Порты можно поправить при необходимости в docker-compose.yml. По умолчанию Compose пробросит два порта на Ваш localhost:
	+ порт 8000 для доступа к wordpress по http;
	+ порт 3306 для доступа к mysql;
 6. В браузере открыть ссылку [http://localhost:8000/](http://localhost:8000/). Должно отобразиться окно начальной настройки WordPress
 7. Выбрать русский язык и нажать продолжить
 8. Заполнить появившуюся форму данными в соответствии с требованиями в программе обучения, например: 
	+ Название сайта – lastname-site-probation
	+ Имя пользователя – Firstname.LastName 
	+ Пароль - 123-Test 
	+ e-mail – firstname.lastname@simbirsoft.com
 9. Нажать кнопку "Установить WordPress"
 10. После установки нажать кнопку "Войти" и ввести введенные ранее учетные данные.
 11. Подключиться к базе данных (например через dbeaver - [https://dbeaver.jkiss.org](https://dbeaver.jkiss.org/) )
- порт 3306
- БД - wordpress
- user – wordpress
- password – wordpress.
 12. Перейти в директорию проекта и открыть командную строку
 13. Выполнить команду `docker ps` и для перехода в контейнер выполнить `docker exec -it <container> bash`
 14. Выполнить команды `apt-get update` и `apt-get install git`
 15. Перейти в каталог `/var/www/html/wp-content/plugins#`
 16. Установить плагин для базовой аутентификации `git clone https://github.com/WP-API/Basic-Auth.git`
 17. Если все прошло успешно должны появиться папка Basic-Auth
 18. Открыть в браузере ссылку [http://localhost:8000/wp-admin/plugins.php](http://localhost:8000/wp-admin/plugins.php) и перейти в раздел ‘Плагины’
 19. Активировать плагин JSON Basic Authentification
 20. Открыть Postman и посмотреть информацию о пользователе (использовать базовую аутентификацию)
 21. Если все шаги выполнены верно, то в запросе отобразится информация о текущем пользователе

## Инструкция по запуску тестов

1. Развернуть проект согласно инструкции
2. Клонировать репозиторий `git clone https://github.com/sdet0mis/ss-api.git`
3. Перейти в директорию репозитория `cd ss-api`
4. Создать виртуальное окружение `python -m venv .venv`
5. Активировать виртуальное окружение `source .venv/bin/activate`
6. Установить зависимости `pip install -r requirements.txt`
7. Запустить тесты `pytest --alluredir=allure-results`
8. Открыть отчет `allure serve allure-results`
