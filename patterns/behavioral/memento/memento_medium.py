class SettingsMemento:
    def __init__(self, **kwargs) -> None:
        self._state = kwargs

    @property
    def theme(self) -> str:
        return self._state["theme"]

    @property
    def language(self) -> str:
        return self._state["language"]


class Settings:
    def __init__(
        self,
        theme: str = "Dark",
        language: str = "Russian",
    ) -> None:
        self.theme = theme
        self.language = language

    def set_theme(self, theme: str) -> None:
        self.theme = theme

    def set_language(self, language: str) -> None:
        self.language = language

    def save(self) -> SettingsMemento:
        return SettingsMemento(theme=self.theme, language=self.language)

    def restore(self, memento: SettingsMemento) -> None:
        self.theme = memento.theme
        self.language = memento.language


class SettingsHistory:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._history: list[SettingsMemento] = [settings.save()]

    def save(
        self,
    ) -> None:
        self._history.append(self._settings.save())

    def undo(self) -> None:
        if not self._history:
            return

        memento = self._history.pop()
        self._settings.restore(memento)


def client_code():
    settings = Settings()
    history = SettingsHistory(settings)

    settings.set_theme("Dark")
    history.save()

    settings.set_language("English")
    history.save()

    print(settings.theme, settings.language)

    history.undo()
    print(settings.theme, settings.language)

    history.undo()
    print(settings.theme, settings.language)
