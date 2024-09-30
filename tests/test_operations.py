from httpx import AsyncClient

async def test_get_movie(ac: AsyncClient):
    response = await ac.get("/operations/data")

    assert response.status_code == 200


async def test_get_movie(ac: AsyncClient):
    response = await ac.get("/operations/data")

    assert response.status_code == 200
