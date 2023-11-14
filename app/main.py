from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse

# from typing import Optional, List

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
        "description": "En un exuberante planeta llamado Pandora viven los Navi, seres que ...",
        "year": 2009,
        "rating": 7.8,
        "category": "Action",
    },
    {
        "id": "2",
        "title": "Avatar",
        "description": "En un exuberante planeta llamado Pandora viven los Navi, seres que ...",
        "year": 2009,
        "rating": 7.8,
        "category": "Action",
    },
]


@app.get(
    "/",
    tags=["Home"],
)
def home() -> HTMLResponse:
    """
    Return a HTMLResponse for home
    """
    return HTMLResponse("<h1>Movies Home</h1>")


@app.get("/movies", tags=["Movies"], response_model=list[MovieSchema])
def get_movies() -> list[MovieSchema]:
    """
    Return a list of dictionaries with information about movies
    """
    return JSONResponse(content=movies)


# Path Param
@app.get("/movies/{id}/", tags=["Movies"], response_model=MovieSchema)
def get_movie_by_id(id: str) -> MovieSchema:
    """
    This endpoint takes a path parameter id to filter the movies.
    """
    movie = [item for item in movies if item["id"] == id]
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return JSONResponse(content=movie[0])


# Query Param
@app.get("/movies/", tags=["Movies"], response_model=list[MovieSchema])
def get_movies_by_category(
    category: str = Query(min_length=2, max_length=50)
) -> list[MovieSchema]:
    """
    This endpoint takes the category as query param
    and returns the filtered list of movies.
    """
    category = category.title()
    data = [movie for movie in movies if movie["category"] == category]
    if not data:
        raise HTTPException(
            status_code=404, detail=f"Movies of the category: '{category}' not found"
        )
    return JSONResponse(content=data)


@app.post("/movies", tags=["Movies"], response_model=dict)
def create_movie(movie: MovieSchema) -> dict:
    movies.append(movie.to_dict())
    return JSONResponse(content={"message": "Movie created successfully"})


@app.put("/movies/{id}", tags=["Movies"], response_model=dict)
def update_movie(id: str, movie: MovieSchema) -> dict:
    for item in movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["description"] = movie.description
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category

    return JSONResponse(content={"message": "Movie updated successfully"})


@app.delete("/movies/{id}", tags=["Movies"], response_model=dict)
def delete_movie(id: str) -> dict:
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)

    return JSONResponse(
        content={"message": f"Movie with Id: '{id}' successfully removed"}
    )
