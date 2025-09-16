from mvc.src.model import MovieModel
from mvc.src.model import IMovieRepository
from mvc.src.model import MovieNotFound


class InMemoryMovieRepository(IMovieRepository):
    def __init__(self):
        self.movies = {}

    def get_movies(self) -> list[MovieModel]:
        return list(self.movies.values())

    def get_movie(self, id: str) -> MovieModel:
        if id not in self.movies:
            raise MovieNotFound(f"Movie with id {id} not found")
        return self.movies[id]

    def add_movie(self, movie: MovieModel) -> None:
        self.movies[movie.id] = movie

    def delete_movie(self, id: str) -> None:
        if id not in self.movies:
            raise MovieNotFound(f"Movie with id {id} not found")
        del self.movies[id]

    def update_movie(self, movie: MovieModel) -> None:
        if movie.id not in self.movies:
            raise MovieNotFound(f"Movie with id {movie.id} not found")
        self.movies[movie.id] = movie
