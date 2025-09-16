from abc import ABC
from abc import abstractmethod

from mvp.src.model import MovieNotFound
from mvp.src.model import MovieModel
from mvp.src.model import IMovieRepository


class InvalidMovieData(Exception):
    pass


class IMovieView(ABC):
    @abstractmethod
    def show_movies(self, movies: list[MovieModel]) -> None:
        pass

    @abstractmethod
    def show_movie(self, movie: MovieModel) -> None:
        pass

    @abstractmethod
    def show_create_movie(self, movie: MovieModel) -> None:
        pass

    @abstractmethod
    def show_delete_movie(self, movie: MovieModel) -> None:
        pass

    @abstractmethod
    def show_update_movie(self, movie: MovieModel) -> None:
        pass

    @abstractmethod
    def show_not_found(self, id: str) -> None:
        pass

    @abstractmethod
    def show_error(self, message: str) -> None:
        pass


class IMoviePresenter(ABC):
    @abstractmethod
    def get_movies(self, view: IMovieView) -> None:
        pass

    @abstractmethod
    def get_movie(self, id: str, view: IMovieView) -> None:
        pass

    @abstractmethod
    def create_movie(self, movie_data: dict, view: IMovieView) -> None:
        pass

    @abstractmethod
    def delete_movie(self, id: str, view: IMovieView) -> None:
        pass

    @abstractmethod
    def update_movie(self, movie_data: dict, view: IMovieView) -> None:
        pass


class MoviePresenter(IMoviePresenter):
    def __init__(self, repository: IMovieRepository) -> None:
        self.repository = repository

    def _validate_movie_data(self, movie_data: dict) -> None:
        required_keys = ["id", "name", "description"]
        missing_keys = [key for key in required_keys if key not in movie_data]
        if len(missing_keys) > 0:
            raise InvalidMovieData(
                f"missing fields: {', '.join(missing_keys)} required"
            )

    def get_movies(self, view: IMovieView) -> None:
        try:
            movies = self.repository.get_movies()
            view.show_movies(movies)
        except Exception as exc:
            view.show_error(str(exc))

    def get_movie(self, id: str, view: IMovieView) -> None:
        try:
            movie = self.repository.get_movie(id)
        except MovieNotFound:
            view.show_not_found(id)
            return
        except Exception as exc:
            view.show_error(str(exc))
            return
        view.show_movie(movie)

    def create_movie(self, movie_data: dict, view: IMovieView) -> None:
        self._validate_movie_data(movie_data)
        movie = MovieModel(
            id=movie_data["id"],
            name=movie_data["name"],
            description=movie_data["description"],
        )
        try:
            self.repository.add_movie(movie)
        except Exception as exc:
            view.show_error(str(exc))
            return
        view.show_create_movie(movie)

    def delete_movie(self, id: str, view: IMovieView) -> None:
        try:
            self.repository.delete_movie(id)
        except MovieNotFound:
            view.show_not_found(id)
            return
        except Exception as exc:
            view.show_error(str(exc))
            return
        view.show_delete_movie(MovieModel(id=id, name="", description=""))

    def update_movie(self, movie_data: dict, view: IMovieView) -> None:
        self._validate_movie_data(movie_data)
        movie = MovieModel(
            id=movie_data["id"],
            name=movie_data["name"],
            description=movie_data["description"],
        )
        try:
            self.repository.update_movie(movie)
        except MovieNotFound:
            view.show_not_found(movie.id)
            return
        except Exception as exc:
            view.show_error(str(exc))
            return
        view.show_update_movie(movie)
