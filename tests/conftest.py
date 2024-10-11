import asyncio
import pytest
from typing import AsyncGenerator
from fastapi.testclient import TestClient
from httpx import AsyncClient

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from src.db import get_async_session
from src.operations.models import metadata as op_metadata
from src.auth.models import metadata as auth_metadata
from src.main import app

from src.config import (TEST_USER, TEST_HOST, 
                        TEST_PORT, TEST_DATABASE, TEST_PASSWORD)

DB_TEST_URL = f"postgresql+asyncpg://{TEST_USER}:{TEST_PASSWORD}@{TEST_HOST}:{TEST_PORT}/{TEST_DATABASE}"

engine_test = create_async_engine(DB_TEST_URL, poolclass=NullPool)
async_session_maker = sessionmaker(bind=engine_test, class_=AsyncSession ,expire_on_commit=False)
op_metadata.bind = engine_test
auth_metadata.bind = engine_test


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[get_async_session] = override_get_async_session

# Create and delete tables
@pytest.fixture(autouse=True, scope="session")
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(auth_metadata.create_all)
        await conn.run_sync(op_metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(auth_metadata.drop_all)
        await conn.run_sync(op_metadata.drop_all)


client = TestClient(app)


# Setup
@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


# Async client
@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

