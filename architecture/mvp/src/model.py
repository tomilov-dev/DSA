from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass


class MovieNotFound(Exception):
    pass


@dataclass
class MovieModel:
    id: str
    name: str
    description: str

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }


class IMovieRepository(ABC):
    @abstractmethod
    def get_movies(self) -> list[MovieModel]:
        pass

    @abstractmethod
    def get_movie(self, id: str) -> MovieModel:
        pass

    @abstractmethod
    def add_movie(self, movie: MovieModel) -> None:
        pass

    @abstractmethod
    def delete_movie(self, id: str) -> None:
        pass

    @abstractmethod
    def update_movie(self, movie: MovieModel) -> None:
        pass
