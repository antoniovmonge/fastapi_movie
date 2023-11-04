from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse

from app.schemas import MovieSchema

app = FastAPI()
app.title = "Movies API"
app.version = "0.0.1"


@app.get("/health-check/", tags=["Health Check"])
def health_check():
    """
    Return just a message to check the app is working.
    """
    return {"message": "OK"}


movies = [
    {
        "id": "1",
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Action",
    },
    {
        "id": "2",
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Action",
    },
]


@app.get("/", tags=["Home"])
def home() -> HTMLResponse:
    """
    Return a HTMLResponse for home
    """
    return HTMLResponse("<h1>Movies Home</h1>")


@app.get("/movies", tags=["Movies"])
def get_movies() -> list:
    """
    Return a list of dictionaries with information about movies
    """
    return JSONResponse(content=movies)


# Path Param
@app.get("/movies/{id}/", tags=["Movies"])
def get_movie_by_id(id: str):
    """
    This endpoint takes a path parameter id to filter the movies.
    """
    movie = [item for item in movies if item["id"] == id]
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


# Query Param
@app.get("/movies/", tags=["Movies"])
def get_movies_by_category(category: str = Query(min_length=2, max_length=50)):
    """
    This endpoint takes the category as query param
    and returns the filtered list of movies.
    """
    category = category.title()
    movies_by_category = [movie for movie in movies if movie["category"] == category]
    if not movies_by_category:
        raise HTTPException(
            status_code=404, detail=f"Movies of the category: '{category}' not found"
        )
    return movies_by_category


@app.post("/movies", tags=["Movies"])
def create_movie(movie: MovieSchema):
    movies.append(movie)
    return movie


@app.put("/movies/{id}", tags=["Movies"])
def update_movie(
    id: str,
    movie: MovieSchema
):
    for item in movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category

    return [item for item in movies if item["id"] == id]



@app.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id: str):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)

    return f"Movie with Id: '{id}' successfully removed"
