# development-tracker-backend

### Технологии:
- Python 3.11
- Django 4.2.7
- Django REST Framework 3.14.0
- djangorestframework-simplejwt 5.3.0
- drf_spectacular 0.26.5
- PostgreSQL 16.1
- gunicorn 21.2.0
- nginx 1.25.3
- Docker 

### Как запустить проект

- клонировать репозиторий

```
git@github.com:hackathon-plus-second-team/development-tracker-backend.git
```

- в домашней директории проекта создать файл .env и наполнить его по примеру .env_sample

```
DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=development_tracker
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=postgres
DB_PORT=5432

DEBUG=True
```

- перейти в директорию infra

```
cd infra 
```

- запустить сборку контейнеров:

```
docker-compose up -d
```

### Предупреждение:

```
Если вы используете Windows, убедитесь, что файл run_app.sh имеет формат конца строки LF
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

### Запустить [frontend](https://github.com/hackathon-plus-second-team/development-tracker-frontend):

- клонировать репозиторий

```
git@github.com:hackathon-plus-second-team/development-tracker-backend.git
```

- запустить сборку контейнеров:

```
docker-compose up -d
```
- проект доступен по адресу:

```
http://localhost:5173/
```

## Авторы

[SunnyInHouse](https://github.com/SunnyInHouse)

[ApriCotBrain](https://github.com/ApriCotBrain)
