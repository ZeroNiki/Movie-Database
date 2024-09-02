from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from src.pages.router import router as rt_pages
from src.operations.router import router as rt_operatinos
from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemas import UserCreate, UserRead


app = FastAPI(
    title="Movie Data Base"
)


@app.get("/")
def main():
    return RedirectResponse("/pages/home")


# Auth
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

# Static
app.mount("/static", StaticFiles(directory="src/static"), name="static")

# Pages
app.include_router(rt_pages)

# Operations
app.include_router(rt_operatinos)
