from abc import ABC
from abc import abstractmethod

from typing import Any
from typing import Dict

from flask import Blueprint
from flask import jsonify
from flask import request
from flask import url_for
from flask import redirect
from flask import escape  # type:ignore

from mvc.src.controller import IMovieController
from mvc.src.model import MovieNotFound


def create_web_blueprint(controller: IMovieController) -> Blueprint:
    """
    Thin web UI blueprint — returns simple HTML pages (no templates).
    View parses form data, calls controller and maps domain errors to HTTP/UI responses.
    """
    bp = Blueprint("web_movies", __name__, url_prefix="/ui")

    @bp.route("/movies", methods=["GET"])
    def list_movies():
        movies = controller.get_movies()
        rows = "".join(
            f"<li><a href='{url_for('web_movies.get_movie', movie_id=escape(m.id))}'>{escape(m.name)}</a></li>"
            for m in movies
        )
        return f"""
            <html><head><meta charset="utf-8"><title>Movies</title></head>
            <body>
                <h1>Movies</h1>
                <ul>{rows}</ul>
                <p><a href="{url_for('web_movies.new_movie_form')}">Create movie</a></p>
            </body></html>
        """

    @bp.route("/movies/<string:movie_id>", methods=["GET"])
    def get_movie(movie_id: str):
        try:
            m = controller.get_movie(movie_id)
        except MovieNotFound:
            return ("Not found", 404)
        return f"""
            <html><head><meta charset="utf-8"><title>{escape(m.name)}</title></head>
            <body>
                <h1>{escape(m.name)}</h1>
                <p>{escape(m.description)}</p>
                <p>ID: {escape(m.id)}</p>
                <form method="post" action="{url_for('web_movies.delete_movie', movie_id=escape(m.id))}">
                    <button type="submit">Delete</button>
                </form>
                <p><a href="{url_for('web_movies.list_movies')}">Back to list</a></p>
            </body></html>
        """

    @bp.route("/movies/new", methods=["GET"])
    def new_movie_form():
        return f"""
            <html><head><meta charset="utf-8"><title>Create movie</title></head>
            <body>
              <h1>Create movie</h1>
              <form method="post" action="{url_for('web_movies.create_movie')}">
                <label>id: <input name="id"></label><br>
                <label>name: <input name="name"></label><br>
                <label>description: <textarea name="description"></textarea></label><br>
                <button type="submit">Create</button>
              </form>
              <p><a href="{url_for('web_movies.list_movies')}">Back</a></p>
            </body></html>
        """

    @bp.route("/movies", methods=["POST"])
    def create_movie():
        data: Dict[str, Any] = {
            "id": (request.form.get("id") or "").strip(),
            "name": (request.form.get("name") or "").strip(),
            "description": (request.form.get("description") or "").strip(),
        }
        if not data["id"] or not data["name"]:
            return ("Bad request", 400)
        controller.create_movie(data)
        return redirect(url_for("web_movies.get_movie", movie_id=data["id"]))

    @bp.route("/movies/<string:movie_id>/delete", methods=["POST"])
    def delete_movie(movie_id: str):
        try:
            controller.delete_movie(movie_id)
        except MovieNotFound:
            return ("Not found", 404)
        return redirect(url_for("web_movies.list_movies"))

    @bp.route("/movies/<string:movie_id>/edit", methods=["GET"])
    def edit_movie_form(movie_id: str):
        try:
            m = controller.get_movie(movie_id)
        except MovieNotFound:
            return ("Not found", 404)
        return f"""
            <html><head><meta charset="utf-8"><title>Edit {escape(m.name)}</title></head>
            <body>
              <h1>Edit movie</h1>
              <form method="post" action="{url_for('web_movies.update_movie', movie_id=escape(m.id))}">
                <label>name: <input name="name" value="{escape(m.name)}"></label><br>
                <label>description: <textarea name="description">{escape(m.description)}</textarea></label><br>
                <button type="submit">Save</button>
              </form>
              <p><a href="{url_for('web_movies.get_movie', movie_id=escape(m.id))}">Cancel</a></p>
            </body></html>
        """

    @bp.route("/movies/<string:movie_id>/edit", methods=["POST"])
    def update_movie(movie_id: str):
        data: Dict[str, Any] = {
            "id": movie_id,
            "name": (request.form.get("name") or "").strip(),
            "description": (request.form.get("description") or "").strip(),
        }
        try:
            controller.update_movie(movie_id, data)
        except MovieNotFound:
            return ("Not found", 404)
        return redirect(url_for("web_movies.get_movie", movie_id=movie_id))

    return bp
