# Серверная часть для [трекера развития](https://github.com/hackathon-plus-second-team)

### Технологии
- Python 3.11
- Django 4.2.7
- Django REST Framework 3.14.0
- djangorestframework-simplejwt 5.3.0
- drf_spectacular 0.26.5
- PostgreSQL 16.1
- gunicorn 21.2.0
- nginx 1.25.3
- Docker 

### Запуск проекта

- клонировать репозиторий

```
git@github.com:hackathon-plus-second-team/development-tracker-backend.git
```

- в директории backend/development_tracker создать файл .env и наполнить его по примеру .env_sample

```
DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=development_tracker
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=postgres
DB_PORT=5432

DEBUG=True
```
### Предупреждение

```
Если вы используете Windows, убедитесь, что файл run_app.sh имеет формат конца строки LF
```

- перейти в директорию infra

```
cd infra 
```

- запустить сборку контейнеров:

```
docker-compose up -d
```

- проект доступен по адресу:

```
http://localhost/
```
- документация доступна по адресу:

```
http://localhost/api/dynamic_doc/swagger/v1/
```

- после запуска проекта в базе данных уже есть пользователь:

```
{
    "email": "TestUser@yandex.ru",
    "password": "ZQj-hBQ-c83-fmu"
}
```
- также есть superuser:

```
{
    "email": "admin@yandex.ru",
    "password": "admin"
}
```

## Авторы

[SunnyInHouse](https://github.com/SunnyInHouse)

[ApriCotBrain](https://github.com/ApriCotBrain)
