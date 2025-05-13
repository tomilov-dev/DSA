"""
Реализация текстового редактора (наивный подход)
"""


class Symbol:
    def __init__(
        self,
        symbol: str,
        font: str,
        color: str,
        posx: int,
        posy: int,
    ) -> None:
        self.symbol = symbol
        self.font = font
        self.color = color
        self.posx = posx
        self.posy = posy

    def __str__(self) -> str:
        return f"{self.symbol}-{self.font}-{self.color}-{self.posx}-{self.posy}"


def client_code():
    fonts = ["A", "B", "C", "D", "E", "F", "G"]
    colors = ["R", "B", "G"]
    symbols = []
    for i in range(len(fonts)):
        for j in range(len(colors)):
            for k in range(100):
                for x in range(256):
                    font = fonts[i]
                    color = colors[j]
                    symbols.append(
                        Symbol(
                            chr(x),
                            font,
                            color,
                            i * j,
                            k * x,
                        )
                    )


if __name__ == "__main__":
    client_code()
