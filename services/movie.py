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
