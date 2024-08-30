from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Optional

from src.operations.models import movies
from src.operations.utils import get_db, format_date

import locale


router = APIRouter(
    prefix="/operations",
    tags=["Operations"]
)


@router.get("/data", response_model=None)
async def get_movies(db: Session = Depends(get_db)):
    try:
        query = select(
            movies.c.title,
            movies.c.vote_average,
            movies.c.poster_path
        ).limit(5)

        result = await db.execute(query)
        data = result.fetchall()

        data_dict = [{
            "title": row[0],
            "vote_average": round(row[1]),
            "poster_path": f"https://image.tmdb.org/t/p/w500{row[2]}"
        } for row in data]

        return data_dict

    except Exception as e:
        return {
            "Message": "Error",
            "Detail": e
        }


@router.get("/search", response_model=None)
async def search_query(
    q: Optional[str] = Query(None, min_length=1, max_length=50),
    db: Session = Depends(get_db)
):
    if q:
        result = await db.execute(
            movies.select().where(movies.c.title.ilike(f"%{q}%"))
        )

        data = result.fetchall()

        if not data:
            raise HTTPException(status_code=404, detail="No movies found")

        return [{
            "title": row.title,
            "overview": row.overview,
            "date": format_date(str(row.release_date)),
            "poster_path": f"https://image.tmdb.org/t/p/w500{row.poster_path}"
        } for row in data]
    else:
        raise HTTPException(status_code=400, detail="Search query is requred")
