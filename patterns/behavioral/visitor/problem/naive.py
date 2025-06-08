"""
Решение задачи на реализацию калькулятора площади через паттерн Посетитель
"""

from abc import ABC
from abc import abstractmethod


class Shape(ABC):
    pass


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height


class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height


class AreaCalculator:
    def calculate(self, shape: Shape) -> None:
        if isinstance(shape, Circle):
            print((shape.radius**2) * 3.14)
        elif isinstance(shape, Rectangle):
            print(shape.width * shape.height)
        elif isinstance(shape, Triangle):
            print(0.5 * shape.base * shape.height)
        else:
            raise ValueError(f"Not implemented shape: {shape.__class__}")


def client_code():
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=6)
    triangle = Triangle(base=3, height=4)

    area_calculator = AreaCalculator()
    area_calculator.calculate(circle)
    area_calculator.calculate(rectangle)
    area_calculator.calculate(triangle)


if __name__ == "__main__":
    client_code()
