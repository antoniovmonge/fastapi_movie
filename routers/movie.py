from fastapi import APIRouter, HTTPException, Query, Depends, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from schemas import MovieSchema
from config.database import Session
from models.movie import Movie
from services.movie import MovieService

from middlewares.jwt_bearer import JWTBearer

movies_router = APIRouter(prefix="/movies", tags=["Movies"])


@movies_router.get(
    "",
    response_model=list[MovieSchema],
    status_code=200,
    dependencies=[Depends(JWTBearer())],
)
def get_movies() -> list[MovieSchema]:
    """
    Return a list of dictionaries with information about movies
    """
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


# Path Param
@movies_router.get("/{id}/", response_model=MovieSchema, status_code=200)
def get_movie_by_id(id: int = Path(ge=1, le=2000)) -> MovieSchema:
    """
    This endpoint takes a path parameter id to filter the movies.
    """
    db = Session()
    result = MovieService(db).get_movie_by_id(id)
    if not result:
        raise HTTPException(status_code=404, detail="Movie not found")
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


# Query Param
@movies_router.get("/", response_model=list[MovieSchema], status_code=200)
def get_movies_by_category(
    category: str = Query(min_length=2, max_length=50)
) -> list[MovieSchema]:
    """
    This endpoint takes the category as query param
    and returns the filtered list of movies.
    """
    category = category.title()
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Movies of the category: '{category}' not found"
        )
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movies_router.post("", response_model=dict, status_code=201)
def create_movie(movie: MovieSchema) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(
        status_code=201, content={"message": "Movie created successfully"}
    )


@movies_router.put("/{id}", response_model=dict, status_code=200)
def update_movie(id: str, movie: MovieSchema) -> dict:
    db = Session()
    MovieService(db).update_movie(id, movie)
    return JSONResponse(
        status_code=200, content={"message": "Movie updated successfully"}
    )


@movies_router.delete("/{id}", response_model=dict, status_code=200)
def delete_movie(id: str) -> dict:
    db = Session()
    MovieService(db).delete_movie(id)
    return JSONResponse(
        status_code=200,
        content={"message": f"Movie with Id: '{id}' successfully removed"},
    )
