from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordRequestForm


from src.operations.router import get_movies, search_query, movie_data
from src.operations.utils import get_db

from src.auth.schemas import UserCreate
from src.auth.base_config import current_user, get_jwt_strategy

from src.pages.schemas import (
    get_user_db_context,
    get_user_manager_context,
    get_async_session_context,
)


router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="src/templates")


@router.get("/home", response_class=HTMLResponse)
async def home_page(request: Request, db=Depends(get_db), user=Depends(current_user)):
    data = await get_movies(db)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "data": data, "user": user}
    )


@router.get("/search", response_class=HTMLResponse)
async def search_page(request: Request, m_data=Depends(search_query), user=Depends(current_user)):
    return templates.TemplateResponse(
        "search.html",
        {
            "request": request,
            "movies": m_data,
            "user": user,
        })


@router.get("/movie/{movie_id}", response_class=HTMLResponse)
async def movie_page(request: Request, m_data=Depends(movie_data), user=Depends(current_user)):
    return templates.TemplateResponse(
        "page.html",
        {
            "request": request,
            "movie": m_data,
            "user": user,
        }
    )


@router.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("sign_up.html", {"request": request})


@router.post("/create")
async def create_user(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):
    async with get_async_session_context() as session:
        async with get_user_db_context(session) as user_db:
            async with get_user_manager_context(user_db) as user_manager:
                user = await user_manager.create(
                    UserCreate(
                        username=username, email=email, password=password
                    )
                )
                print(f"User was created {user}")

    response = RedirectResponse(url="/pages/login/")
    response.status_code = 302
    return response


@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("sign_in.html", {"request": request})


@router.post("/login")
async def login_user(email: str = Form(...), password: str = Form(...)):
    async with get_async_session_context() as session:
        async with get_user_db_context(session) as user_db:
            async with get_user_manager_context(user_db) as user_manager:
                credentials = OAuth2PasswordRequestForm(
                    username=email, password=password)
                user = await user_manager.authenticate(credentials)

                if not user:
                    return {
                        "Message": "Error",
                        "Detail": "User not found",
                        "Solution": "Go back and enter correct email and password"
                    }

                jwt_strg = get_jwt_strategy()
                token = await jwt_strg.write_token(user)

    response = RedirectResponse(url="/pages/home/")
    response.set_cookie(key="auth_token", value=token, httponly=True)
    response.status_code = 302
    return response


@router.post("/logout")
async def logout_user(request: Request):
    response = RedirectResponse("/pages/home/")
    response.set_cookie(key="auth_token")
    response.status_code = 302
    return response
