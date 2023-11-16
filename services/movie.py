from fastapi import HTTPException
from models.movie import Movie


class MovieService:
    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        result = self.db.query(Movie).all()
        return result

    def get_movie_by_id(self, id: int):
        result = self.db.query(Movie).filter(Movie.id == id).first()
        return result

    def get_movies_by_category(self, category: str):
        result = self.db.query(Movie).filter(Movie.category == category).all()
        return result

    def create_movie(self, movie: Movie):
        new_movie = Movie(**movie.model_dump())
        self.db.add(new_movie)
        self.db.commit()
        return None

    def update_movie(self, id: int, movie: Movie):
        result = self.get_movie_by_id(id)
        if not result:
            raise HTTPException(status_code=404, detail="Movie not found")
        result.title = movie.title
        result.description = movie.description
        result.year = movie.year
        result.rating = movie.rating
        result.category = movie.category
        self.db.commit()
        return None

    def delete_movie(self, id: int):
        result = self.get_movie_by_id(id)
        if not result:
            raise HTTPException(status_code=404, detail="Movie not found")
        self.db.delete(result)
        self.db.commit()
        return None
