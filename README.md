# Тестовое задание на должность Python Backend Developer

Необходимо создать сервер авторизации и новостей с комментариями и лайкаами на Django с использованием
RestFramework на Python 3.

* У каждого пользователя может быть две роли – пользователь и админ, админ может зайти в админ-панель, пользователь – нет. Как 
именно решить эту задачу не принципиально. Плюсом будет создание кастомного класса для авторизации наследуемого от BaseAuthentication - нам важно видеть как вы решите эту задачу.

* Каждый пользователь может создать новость. Все пользователи могут получать списки всех новостей с пагинацией. Пользователи могут 
удалять и изменять свои новости. Админ может удалять и изменять любую новость.

* Также нужно добавить механизм лайков и комментариев новостей – лайкать и комментировать может любой пользователь, автор может 
удалять комментарии к своим новостям, админ может удалять любые комментарии. 
При получении списка новостей и одной конкретной новости нужно показать количество лайков и комментариев. Плюсом будет 
добавление списка последних 10 комментариев при получении списка новостей и одной новости.
Плюсом будет реализация механизма через микросервис.

## Желательно:
* контейнеризация в Docker
* использование Python Venv
* использование Web сервера CherryPy, gunicorn и им подобных (какого-нибудь одного)
* демонстрация понимания механизма миграций моделей (можно сделать несколько изменений в какой-либо модели и показать миграции)
* использование .env файла для хранения инфомрации о подключении к базе данных
* файл README.md с описанием скриптов для разворачивания окружения и запуска сервера

## Модели:
* Users (имя пользователя, пароль в зашифрованном виде)
* News (дата новости, заголовок новости, текст новости, автор)
* Comments (дата комментария, текст комментария, автор)
* Опционально: Tokens (при авторизации можно создавать токены и хранить их в базе данных или использовать JWT токены)

## Роуты:
* POST auth (передаём имя пользователя и пароль, получаем токен, если пользователь с таким паролем есть и ошибку, если такого пользователя нет)
* GET news (получаем список новостей с пагинацией)
* POST news (создаём новость, проверка на авторизацию)
* PUT news (обновляем новость, проверка на авторизацию, проверка на наличие прав)
* DELETE news 
* GET comments (получение списка комментариев новости с пагинацией)
* POST comments (создание нового комментария, проверка на авторизацию)
* DELETE comments

## Админка:
* Нужна стандартная админка Django (пользователи админки могут не пересекаться с пользователями в табилце Users)

# Разворачивание окружения и запуск сервера
1. Создать файл .env в директории проекта и прописать необходимые параметры: SECRET_KEY, PG_HOST, PG_DATABASE, PG_USER, PG_PASSWORD, PG_PORT.
2. В директории проекта использовать команду ***docker-compose build && docker-compose up -d*** для сборки образов приложения и запуска их в фоновом режиме.
3. С помощью команды ***docker exec -it news_service bash*** зайти в контейнер и выполнить команду ***python manage.py migrate*** для применения миграций базы данных.
4. После запуска приложения оно будет доступно по адресу **0.0.0.0:8000**.
    