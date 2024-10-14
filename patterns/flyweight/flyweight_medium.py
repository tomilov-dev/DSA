from abc import ABC
from abc import abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self) -> str:
        pass


class Circle(Shape):
    def __init__(
        self,
        radius: float,
        color: str,
    ) -> None:
        self.__radius = radius
        self.__color = color

    def draw(self) -> str:
        return f"Circle with radius {self.__radius} and color {self.__color}"


class ShapeFactory:
    def __init__(self) -> None:
        self._circles = dict()

    def get_circle(self, radius: float, color: str) -> Circle:
        key = (radius, color)
        if key not in self._circles:
            self._circles[key] = Circle(radius, color)
        return self._circles[key]


class ShapeContext(ABC):
    def __init__(
        self,
        x: float,
        y: float,
        shape: Shape,
    ) -> None:
        self.x = x
        self.y = y
        self.shape = shape


class CircleContext(ShapeContext):
    def draw(self) -> str:
        shape = self.shape.draw()
        return f"{shape} at coordinates ({self.x}, {self.y})"


def client_code():
    factory = ShapeFactory()

    context1 = CircleContext(5, 5, factory.get_circle(10, "Red"))
    context2 = CircleContext(15, 15, factory.get_circle(20, "Blue"))
    context3 = CircleContext(25, 25, factory.get_circle(10, "Red"))

    print(context1.draw())
    print(context2.draw())
    print(context3.draw())
