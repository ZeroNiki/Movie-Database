# База данных фильмов

## Навигация

- [О проекте](#О проекте)
- [Установить](#Установить)
- [О базе данных](#О-базе-данных)
- [Миграции Alembic](#Alembic-migrations)
- [Откуда я взял данные?](#Откуда-я-получил-данные?)
- [Архитектура проекта](#Архитектура-проекта)
- [Маршруты](#Маршруты)
- [TODO](#TODO)

## О проекте

lib:

- fastapi
- fastapi_users
- sqlalchemy (для postgresql)
- alembic

Это веб-приложение для показа фильмов. Можно зарегистрировать и авторизовать пользователя

## Установить

```bash
git clone https://github.com/ZeroNiki/Movie-Database.git
cd git
```

<img src="https://github.com/ZeroNiki/Movie-Database/blob/main/media/render_git.gif" alt="Alt text" width="800" height="500">

настроить файл [.env](https://github.com/ZeroNiki/Movie-Database/blob/main/.env):

```
DATABASE=xxxx
USER=xxxx
HOST=xxxx
PASSWORD=xxxx
PORT=xxxx

AUTH_TOKEN=xxxx
```

`Database` - Имя вашей базы данных
`User` - Пользователь вашей базы данных
`HOST` - Хост вашей базы данных (по умолчанию `localhost`)
`PASSWORD` - Пароль вашей базы данных (по умолчанию `postgres`)
`PORT` - Порт вашей базы данных (по умолчанию `5432`)

`AUTH_TOKEN` - Здесь вы можете использовать генератор токенов

Создайте виртуальную среду:

```bash
python3 -m venv venv

source venv/bin/activate
```

Если вы используете Windows 10:

```bash
python -m venv venv

venv\Scripts\activate
```

После настройки файла [.env](https://github.com/ZeroNiki/Movie-Database/blob/main/.env) и создания venv вы можете запустить приложение:

```bash
uvicorn src.main:app --reload
```

<img src="https://github.com/ZeroNiki/Movie-Database/blob/main/media/render_uvicorn.gif" alt="Alt text" width="800" height="500">

перейти на http://127.0.0.1:8000

## О базе данных

**PostgreSQL** используется в качестве базы данных
Шаблон bd находится в [Database example](https://github.com/ZeroNiki/Movie-Database/tree/main/Database%20example) dir

### Миграции Alembic

```bash
alembic revision --autogenerate -m "First init"

alembic upgrade head
```

### Откуда я взял данные?

Взято из API этого [ресурса](https://developer.themoviedb.org/docs/getting-started)

## Архитектура проекта

```
src
├── auth
│   └── ...
├── operations
│   └── ...
├── pages
│   └── ...
├── static
│   ├── css
│   │└── ...
│   └── Favicon
│   └── ...
└── templates
└── ...
```

`src/auth` - Все в этой папке предназначено для авторизации пользователя<br>
`src/operations` - Предназначено для взаимодействия с базой данных<br>
`src/pages` - Для страниц<br>
`src/static` - Для статических файлов (css, js, медиаконтент)<br>
`src/templates` - Для html<br>

### Маршруты

`/pages/home/` - домашняя страница<br>
`/pages/search?q={keyword}` - Страница поиска<br>
`/pages/movie/{movie_id}` - страница фильма<br>
`/pages/register` - страница регистрации<br>
`/pages/login` - страница входа<br>

## TODO

- [ ] 5 сентября 2024 г. `Завершить роль для пользователей`
- [x] 4 сентября 2024 г. `Исправить незначительные ошибки в навигации`
- [x] 2 сентября 2024 г. `Связать аутентификацию с интерфейсом`
- [x] 2 сентября 2024 г. `Добавить аутентификацию`
- [x] 1 сентября 2024 г. `Завершить /pages/movie/{id}`
- [x] 30 августа 2024 г. `Исправить отображаемый текст в /pages/search?q={query}`
