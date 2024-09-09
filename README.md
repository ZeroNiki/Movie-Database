# Movie Database

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

configure `.env` file:

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

## TODO

- [ ] 5 September 2024 `Finalize role for users`
- [x] 4 September 2024 `Fix minor bugs in nav`
- [x] 2 September 2024 `link auth to front-end`
- [x] 2 September 2024 `Add auth`
- [x] 1 September 2024 `Finalize the /pages/movie/{id}`
- [x] 30 August 2024 `Fix the display text in /pages/search?q={query}`
