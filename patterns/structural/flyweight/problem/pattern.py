"""
Реализация текстового редактора через паттерн Легковес
"""


class CharStyle:
    def __init__(self, font: str, color: str) -> None:
        self.font = font
        self.color = color


class CharStyleFactory:
    def __init__(
        self,
        storage: dict[tuple[str, str], CharStyle] | None = None,
    ) -> None:
        if storage is None:
            storage = {}
        self.storage = storage

    def get(self, font: str, color: str) -> CharStyle:
        key = (font, color)
        if key not in self.storage:
            self.storage[key] = CharStyle(font, color)
        return self.storage[key]


class Symbol:
    def __init__(
        self,
        symbol: str,
        style: CharStyle,
        posx: int,
        posy: int,
    ) -> None:
        self.symbol = symbol
        self.style = style
        self.posx = posx
        self.posy = posy

    def __str__(self) -> str:
        return f"{self.symbol}-{self.style.font}-{self.style.color}-{self.posx}-{self.posy}"


def client_code():
    fonts = ["A", "B", "C", "D", "E", "F", "G"]
    colors = ["R", "B", "G"]
    factory = CharStyleFactory()
    symbols = []
    for i in range(len(fonts)):
        for j in range(len(colors)):
            for k in range(100):
                for x in range(256):
                    font = fonts[i]
                    color = colors[j]
                    style = factory.get(font, color)
                    symbols.append(
                        Symbol(
                            chr(x),
                            style,
                            i * j,
                            k * x,
                        )
                    )


if __name__ == "__main__":
    client_code()
