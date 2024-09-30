from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from typing import AsyncGenerator


from src.config import DATABASE, HOST, USER, PORT, PASSWORD

DATABASE_URL = f"postgresql+asyncpg://{
    USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
print(DATABASE_URL)

engine = create_async_engine(DATABASE_URL, poolclass=NullPool)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    future=True,
)

Base = declarative_base()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
