from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Optional

from src.operations.models import movies
from src.operations.utils import get_db, format_date

router = APIRouter(
    prefix="/operations",
    tags=["Operations"]
)


# This is only for home page
@router.get("/data", response_model=None)
async def get_movies(db: Session = Depends(get_db)):
    try:
        query = select(
            movies.c.id,
            movies.c.title,
            movies.c.vote_average,
            movies.c.poster_path,
        ).limit(5)

        result = await db.execute(query)
        data = result.fetchall()

        data_dict = [{
            "id": row[0],
            "title": row[1],
            "vote_average": round(row[2]),
            "poster_path": f"https://image.tmdb.org/t/p/w500{row[3]}"
        } for row in data]

        return data_dict

    except Exception as e:
        return {
            "Message": "Error",
            "Detail": e
        }


@router.get("/search", response_model=None)
async def search_query(
    q: Optional[str] = Query(None, max_length=50),
    db: Session = Depends(get_db)
):

    result = await db.execute(
        movies.select().where(movies.c.title.ilike(f"%{q}%"))
    )

    data = result.fetchall()

    if not data:
        return ["Not found"]

    return [{
        "id": row.id,
        "title": row.title,
        "overview": row.overview,
        "date": format_date(str(row.release_date)),
        "poster_path": f"https://image.tmdb.org/t/p/w500{row.poster_path}"
    } for row in data]


# This for personal movie page
@router.get("/{movie_id}")
async def movie_data(movie_id: int, db: Session = Depends(get_db)):
    try:
        result = await db.execute(
            movies.select().where(movies.c.id == movie_id)
        )

        data = result.fetchall()

        if not data:
            return ["Not found"]

        return [{
            "id": row.id,
            "title": row.title,
            "original_title": row.original_title,
            "date": format_date(str(row.release_date)),
            "overview": row.overview,
            "vote_average": round(row.vote_average),
            "poster_path": f"https://image.tmdb.org/t/p/w500{row.poster_path}"
        } for row in data]

    except Exception as e:
        return {
            "Message": "Error",
            "Detail": e
        }
