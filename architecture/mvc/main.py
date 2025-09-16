from flask import Flask

from mvc.src.repository import InMemoryMovieRepository
from mvc.src.controller import MovieController
from mvc.src.views.api.api import create_api_blueprint
from mvc.src.views.web.web import create_web_blueprint


def create_app():
    app = Flask(__name__)
    repo = InMemoryMovieRepository()
    controller = MovieController(repo)

    api_bp = create_api_blueprint(controller)
    web_bp = create_web_blueprint(controller)

    app.register_blueprint(api_bp)
    app.register_blueprint(web_bp)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
