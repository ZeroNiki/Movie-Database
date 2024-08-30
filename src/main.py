from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from src.pages.router import router as rt_pages
from src.operations.router import router as rt_operatinos


app = FastAPI(
    title="Movie Data Base"
)


@app.get("/")
def main():
    return RedirectResponse("/pages/home")


# Static
app.mount("/static", StaticFiles(directory="src/static"), name="static")

# Pages
app.include_router(rt_pages)

# Operations
app.include_router(rt_operatinos)
