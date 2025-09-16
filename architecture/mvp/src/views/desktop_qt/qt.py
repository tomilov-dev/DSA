from typing import Dict

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QListWidget
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QTextEdit
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QFormLayout
from PySide6.QtWidgets import QDialogButtonBox

from mvp.src.model import MovieModel
from mvp.src.presenter import IMovieView


class MovieDialog(QDialog):
    def __init__(
        self,
        parent=None,
        movie: MovieModel | None = None,
        id_editable: bool = True,
    ) -> None:
        super().__init__(parent)
        self.setWindowTitle("Movie")
        self._id_editable = id_editable
        self.id_input = QLineEdit(movie.id if movie else "")
        self.id_input.setEnabled(id_editable)
        self.name_input = QLineEdit(movie.name if movie else "")
        self.desc_input = QTextEdit(movie.description if movie else "")
        form = QFormLayout()
        form.addRow("ID:", self.id_input)
        form.addRow("Name:", self.name_input)
        form.addRow("Description:", self.desc_input)
        btns = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        btns.accepted.connect(self.accept)
        btns.rejected.connect(self.reject)
        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(btns)
        self.setLayout(layout)

    def data(self) -> dict[str, str]:
        return {
            "id": self.id_input.text().strip(),
            "name": self.name_input.text().strip(),
            "description": self.desc_input.toPlainText().strip(),
        }


class QTDesktopMovieView(QMainWindow, IMovieView):
    def __init__(self, presenter):
        super().__init__()
        self.presenter = presenter
        self.setWindowTitle("Movies (MVP demo)")
        self._movies_by_id: Dict[str, MovieModel] = {}

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout()
        central.setLayout(layout)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        btn_layout = QHBoxLayout()
        layout.addLayout(btn_layout)
        self.btn_new = QPushButton("New")
        self.btn_edit = QPushButton("Edit")
        self.btn_delete = QPushButton("Delete")
        self.btn_refresh = QPushButton("Refresh")
        btn_layout.addWidget(self.btn_new)
        btn_layout.addWidget(self.btn_edit)
        btn_layout.addWidget(self.btn_delete)
        btn_layout.addWidget(self.btn_refresh)

        self.btn_new.clicked.connect(self.on_new)
        self.btn_edit.clicked.connect(self.on_edit)
        self.btn_delete.clicked.connect(self.on_delete)
        self.btn_refresh.clicked.connect(lambda: self.presenter.get_movies(self))
        self.list_widget.itemDoubleClicked.connect(self.on_double_click)

        self.presenter.get_movies(self)

    def _selected_id(self) -> str | None:
        item = self.list_widget.currentItem()
        if item is None:
            return None
        return item.data(Qt.ItemDataRole.UserRole)

    def show_movies(self, movies) -> None:
        self._movies_by_id = {m.id: m for m in movies}
        self.list_widget.clear()
        for m in movies:
            item = m.name
            lw_item = self.list_widget.addItem(item)  # type: ignore

        for idx, m in enumerate(movies):
            it = self.list_widget.item(idx)
            it.setData(Qt.ItemDataRole.UserRole, m.id)

    def show_movie(self, movie: MovieModel) -> None:
        QMessageBox.information(
            self,
            f"{movie.name}",
            f"Name: {movie.name}\n\nDescription:\n{movie.description}\n\nID: {movie.id}",
        )

    def show_create_movie(self, movie: MovieModel) -> None:
        QMessageBox.information(self, "Created", f"Movie {movie.id} created")
        self.presenter.get_movies(self)

    def show_delete_movie(self, movie: MovieModel) -> None:
        QMessageBox.information(self, "Deleted", f"Movie {movie.id} deleted")
        self.presenter.get_movies(self)

    def show_update_movie(self, movie: MovieModel) -> None:
        QMessageBox.information(self, "Updated", f"Movie {movie.id} updated")
        self.presenter.get_movies(self)

    def show_not_found(self, id: str) -> None:
        QMessageBox.warning(self, "Not found", f"Movie {id} not found")

    def show_error(self, message: str) -> None:
        QMessageBox.critical(self, "Error", message)

    def on_new(self):
        dlg = MovieDialog(self)
        if dlg.exec() != QDialog.DialogCode.Accepted:
            return
        data = dlg.data()
        self.presenter.create_movie(data, self)

    def on_edit(self):
        sel = self._selected_id()
        if not sel:
            QMessageBox.information(self, "Select", "Select a movie first")
            return
        try:
            self.presenter.get_movie(sel, self)
            m = self._movies_by_id.get(sel)
            if m is None:
                return
            dlg = MovieDialog(self, movie=m, id_editable=False)
            if dlg.exec() != QDialog.DialogCode.Accepted:
                return
            data = dlg.data()
            self.presenter.update_movie(data, self)
        except Exception:
            pass

    def on_delete(self):
        sel = self._selected_id()
        if not sel:
            QMessageBox.information(self, "Select", "Select a movie first")
            return
        confirm = QMessageBox.question(self, "Confirm", f"Delete movie {sel}?")
        if confirm != QMessageBox.StandardButton.Yes:
            return
        self.presenter.delete_movie(sel, self)

    def on_double_click(self, item):
        movie_id = item.data(Qt.ItemDataRole.UserRole)
        if movie_id:
            self.presenter.get_movie(movie_id, self)
