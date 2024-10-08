# Movie Database

## Navigation

[RU README.md](https://github.com/ZeroNiki/Movie-Database/blob/main/RU_README.md)

- [About](#About)
- [Install](#Install)
- [About the database](#About-the-database)
  - [Alembic migrations](#Alembic-migrations)
  - [Where did I get the data from?](#Where-did-I-get-the-data-from?)
- [Architecture of the project](#Architecture-of-the-project)
  - [Routes](#Routes)
- [TODO](#TODO)

## About

lib:

- fastapi
- fastapi_users
- sqlalchemy (for postgresql)
- alembic

This is a web application for displaying movies. It is possible to register and authorize the user

## Install

```bash
git clone https://github.com/ZeroNiki/Movie-Database.git
cd git
```

<img src="https://github.com/ZeroNiki/Movie-Database/blob/main/media/render_git.gif" alt="Alt text" width="800" height="500">

configure [.env](https://github.com/ZeroNiki/Movie-Database/blob/main/.env) file:

```
DATABASE=xxxx
USER=xxxx
HOST=xxxx
PASSWORD=xxxx
PORT=xxxx

AUTH_TOKEN=xxxx
```

`Database` - Name of your database
`User` - User of your database
`HOST` - Host of your database (by default `localhost`)
`PASSWORD` - Password of your database (by default `postgres`)
`PORT` - Port of your database (by default `5432`)

`AUTH_TOKEN` - Here you can use the token generator

Create virtual environment:

```bash
python3 -m venv venv

pip install -r requirements.txt

source venv/bin/activate
```

If you use Windows 10:

```bash
python -m venv venv

pip install -r requirements.txt

venv\Scripts\activate
```

Once you have configured the [.env](https://github.com/ZeroNiki/Movie-Database/blob/main/.env) file and create venv you can start running the application:

```bash
uvicorn src.main:app --reload
```

<img src="https://github.com/ZeroNiki/Movie-Database/blob/main/media/render_uvicorn.gif" alt="Alt text" width="800" height="500">

go to http://127.0.0.1:8000

## About the database

**PostgreSQL** is used as a database
The bd template is found in [Database example](https://github.com/ZeroNiki/Movie-Database/tree/main/Database%20example) dir

### Alembic migrations

**first create a directory `versions` in `migrations/`**

```bash
mkdir migrations/versions

alembic revision --autogenerate -m "First init"

alembic upgrade head
```

### Where did I get the data from?

Taken from the API of this [resource](https://developer.themoviedb.org/docs/getting-started)

## Architecture of the project

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
   │   │   └── ...
   │   └── Favicon
   │       └── ...
   └── templates
       └── ...
```

`src/auth` - Everything in this folder is intended for user authorization<br>
`src/operations` - Designed for interaction with the database<br>
`src/pages` - For pages<br>
`src/static` - For static files (css, js, media content)<br>
`src/templates` - For html<br>

### Routes

`/pages/home/` - home page<br>
`/pages/search?q={keyword}` - search page<br>
`/pages/movie/{movie_id}` - movie page<br>
`/pages/register` - Signup page<br>
`/pages/login` - Login page<br>

## TODO

- [ ] 5 September 2024 `Finalize role for users`
- [x] 4 September 2024 `Fix minor bugs in nav`
- [x] 2 September 2024 `link auth to front-end`
- [x] 2 September 2024 `Add auth`
- [x] 1 September 2024 `Finalize the /pages/movie/{id}`
- [x] 30 August 2024 `Fix the display text in /pages/search?q={query}`
