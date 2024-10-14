import copy
from abc import ABC
from abc import abstractmethod


class Shape(ABC):
    @abstractmethod
    def clone(self) -> "Shape":
        pass


class Circle(Shape):
    def __init__(
        self,
        radius: float,
        color: str,
    ) -> None:
        self.radius = radius
        self.color = color

    def clone(self) -> "Circle":
        return copy.copy(self)

    def __str__(self) -> str:
        return f"Circle(radius={self.radius}, color={self.color})"


class Rectangle(Shape):
    def __init__(
        self,
        width: float,
        height: float,
        color: str,
    ) -> None:
        self.width = width
        self.height = height
        self.color = color

    def clone(self) -> "Rectangle":
        return copy.copy(self)

    def __str__(self) -> str:
        return (
            f"Rectangle(width={self.width}, height={self.height}, color={self.color})"
        )


def client_code():
    rec1 = Rectangle(10, 20, "red")
    rec2 = Rectangle(30, 30, "blue")
    rec3 = rec1.clone()
    rec4 = rec1.clone()

    assert rec3.width == rec4.width
    assert rec3.height == rec4.height


if __name__ == "__main__":
    client_code()
