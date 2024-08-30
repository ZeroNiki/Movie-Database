from datetime import datetime

from src.db import AsyncSessionLocal


async def get_db():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()


def format_date(date_str: str) -> str:
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    formatted_date = date_obj.strftime('%d %B %Y')
    return formatted_date
