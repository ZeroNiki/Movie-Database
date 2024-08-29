from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="src/templates")


@router.get("/home")
def home_page(request: Request):
    links = [
        {'url': 'https://image.tmdb.org/t/p/w500/8cdWjvZQUExUUTzyp4t6EDMubfO.jpg',
            'name': "Deadpool & Wolverine", "rating": round(7.77)},
        {'url': 'https://image.tmdb.org/t/p/w500/vpnVM9B6NMmQpWeZvzLvDESb2QY.jpg',
            'name': "Inside Out 2", "rating": round(7.685)},
        {'url': 'https://image.tmdb.org/t/p/w500/wWba3TaojhK7NdycRhoQpsG0FaH.jpg',
            'name': "Despicable Me 4", "rating": round(7.3)},
        {'url': 'https://image.tmdb.org/t/p/w500/pjnD08FlMAIXsfOLKQbvmO0f0MD.jpg',
            'name': "Twisters", "rating": round(7.046)},
        {'url': 'https://image.tmdb.org/t/p/w500/d9CTnTHip1RbVi2OQbA2LJJQAGI.jpg',
            'name': "The Union", "rating": round(6.347)},
    ]

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "links": links}
    )
