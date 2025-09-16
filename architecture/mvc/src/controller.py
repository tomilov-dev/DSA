from abc import ABC
from abc import abstractmethod
from mvc.src.model import MovieModel
from mvc.src.model import IMovieRepository


class IMovieController(ABC):
    @abstractmethod
    def get_movies(self) -> list[MovieModel]:
        pass

    @abstractmethod
    def get_movie(self, id: str) -> MovieModel:
        pass

    @abstractmethod
    def create_movie(self, movie_data: dict) -> None:
        pass

    @abstractmethod
    def delete_movie(self, id: str) -> None:
        pass

    @abstractmethod
    def update_movie(self, id: str, movie_data: dict) -> None:
        pass


class MovieController(IMovieController):
    def __init__(self, repository: IMovieRepository):
        self.repository = repository

    def get_movies(self) -> list[MovieModel]:
        return self.repository.get_movies()

    def get_movie(self, id: str) -> MovieModel:
        return self.repository.get_movie(id)

    def create_movie(self, movie_data: dict) -> None:
        movie_model = MovieModel(
            id=movie_data["id"],
            name=movie_data["name"],
            description=movie_data["description"],
        )
        self.repository.add_movie(movie_model)

    def delete_movie(self, id: str) -> None:
        self.repository.delete_movie(id)

    def update_movie(self, id: str, movie_data: dict) -> None:
        movie_model = MovieModel(
            id=movie_data["id"],
            name=movie_data["name"],
            description=movie_data["description"],
        )
        self.repository.update_movie(movie_model)
