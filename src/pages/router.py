from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.operations.router import get_movies, search_query, movie_data
from src.operations.utils import get_db


router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="src/templates")


@router.get("/home", response_class=HTMLResponse)
async def home_page(request: Request, db=Depends(get_db)):
    data = await get_movies(db)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "data": data}
    )


@router.get("/search", response_class=HTMLResponse)
async def search_page(request: Request, m_data=Depends(search_query)):
    return templates.TemplateResponse(
        "search.html",
        {
            "request": request,
            "movies": m_data,
        })


@router.get("/movie/{movie_id}", response_class=HTMLResponse)
async def movie_page(request: Request, m_data=Depends(movie_data)):
    return templates.TemplateResponse(
        "page.html",
        {
            "request": request,
            "movie": m_data
        }
    )


@router.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("sign_up.html", {"request": request})


@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("sign_in.html", {"request": request})
