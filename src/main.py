from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.pages.router import router as rt_pages


app = FastAPI(
    title="Movie Data Base"
)

# Static
app.mount("/static", StaticFiles(directory="src/static"), name="static")

# Pages
app.include_router(rt_pages)
