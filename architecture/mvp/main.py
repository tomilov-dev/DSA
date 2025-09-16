import sys

from mvp.src.repository import InMemoryMovieRepository
from mvp.src.presenter import MoviePresenter
from mvp.src.views.desktop_qt.qt import QTDesktopMovieView

from PySide6.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    repo = InMemoryMovieRepository()
    presenter = MoviePresenter(repo)
    window = QTDesktopMovieView(presenter)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
