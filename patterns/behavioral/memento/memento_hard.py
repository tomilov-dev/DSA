class GameStateMemento:
    def __init__(self, level: int, score: int, health: int) -> None:
        self.level = level
        self.score = score
        self.health = health


class GameState:
    def __init__(self, level: int, score: int, health: int) -> None:
        self.level = level
        self.score = score
        self.health = health

    def set_level(self, level: int) -> None:
        self.level = level

    def set_score(self, score: int) -> None:
        self.score = score

    def set_health(self, health: int) -> None:
        self.health = health

    def save(self) -> GameStateMemento:
        return GameStateMemento(self.level, self.score, self.health)

    def restore(self, memento: GameStateMemento) -> None:
        self.level = memento.level
        self.score = memento.score
        self.health = memento.health


class GameStateHistory:
    def __init__(self, game_state: GameState) -> None:
        self._game_state = game_state
        self._history: list[GameStateMemento] = [game_state.save()]

    def save(
        self,
    ) -> None:
        self._history.append(self._game_state.save())

    def undo(self) -> None:
        if not self._history:
            return

        memento = self._history.pop()
        self._game_state.restore(memento)
