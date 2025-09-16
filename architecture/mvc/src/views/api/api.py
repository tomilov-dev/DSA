from typing import Any
from typing import Dict

from flask import Blueprint
from flask import jsonify
from flask import request
from flask import url_for

from mvc.src.controller import IMovieController
from mvc.src.model import MovieNotFound


def create_api_blueprint(controller: IMovieController) -> Blueprint:
    bp = Blueprint("api_movies", __name__, url_prefix="/api")

    @bp.route("/movies", methods=["GET"])
    def list_movies():
        movies = controller.get_movies()
        return jsonify([m.to_dict() for m in movies])

    @bp.route("/movies/<string:movie_id>", methods=["GET"])
    def get_movie(movie_id: str):
        try:
            m = controller.get_movie(movie_id)
        except MovieNotFound:
            return ("Not found", 404)
        return jsonify(m.to_dict())

    @bp.route("/movies", methods=["POST"])
    def create_movie():
        data: Dict[str, Any] = request.get_json() or {}
        if not all(k in data for k in ("id", "name", "description")):
            return ("Bad request", 400)
        controller.create_movie(data)
        location = url_for("api_movies.get_movie", movie_id=data["id"])
        return ("", 201, {"Location": location})

    @bp.route("/movies/<string:movie_id>", methods=["DELETE"])
    def delete_movie(movie_id: str):
        try:
            controller.delete_movie(movie_id)
        except MovieNotFound:
            return ("Not found", 404)
        return ("", 204)

    @bp.route("/movies/<string:movie_id>", methods=["PUT"])
    def update_movie(movie_id: str):
        data: Dict[str, Any] = request.get_json() or {}
        data["id"] = movie_id
        try:
            controller.update_movie(movie_id, data)
        except MovieNotFound:
            return ("Not found", 404)
        return ("", 204)

    return bp
