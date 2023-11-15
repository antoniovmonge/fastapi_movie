from fastapi import FastAPI
from fastapi.responses import HTMLResponse



from config.database import engine, Base
from routers import movies_router, users_router


from middlewares.error_handler import ErrorHandler

app = FastAPI()
app.title = "Movies API"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(users_router)
app.include_router(movies_router)

Base.metadata.create_all(bind=engine)


@app.get("/health-check/", tags=["Health Check"])
def health_check():
    """
    Return just a message to check the app is working.
    """
    return {"message": "OK"}


@app.get(
    "/",
    tags=["Home"],
)
def home() -> HTMLResponse:
    """
    Return a HTMLResponse for home
    """
    return HTMLResponse("<h1>Movies Home</h1>")
