# development-tracker-backend

### Как запустить проект(development version)

- клонировать репозиторий

```
git@github.com:hackathon-plus-second-team/development-tracker-backend.git
```

- перейти в ветку develop и загрузить актуальные изменения

```
git checkout develop origin/develop
git pull
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

- проект доступен по адресу:

```
http://localhost/
```
- документация доступна по адресу:

```
http://localhost/api/dynamic_doc/swagger/v1/
```

- после запуска проекта в базе данных уже есть пользователь с оплаченными курсами:

```
{
    "email": "TestUser@yandex.ru",
    "password": "ZQj-hBQ-c83-fmu"
}
```
