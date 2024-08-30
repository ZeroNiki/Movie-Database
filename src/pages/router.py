from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from typing import Optional
from fastapi.templating import Jinja2Templates

from src.operations.router import get_movies, search_query
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
async def search_page(request: Request, movie_data=Depends(search_query)):
    return templates.TemplateResponse(
        "search.html",
        {
            "request": request,
            "movies": movie_data,
        })
