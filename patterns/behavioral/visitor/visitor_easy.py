from abc import ABC
from abc import abstractmethod


class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: "Visitor") -> None:
        pass


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def accept(self, visitor: "Visitor") -> None:
        visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def accept(self, visitor: "Visitor") -> None:
        visitor.visit_rectangle(self)


class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def accept(self, visitor: "Visitor") -> None:
        visitor.visit_triangle(self)


class Visitor(ABC):
    @abstractmethod
    def visit_circle(self, circle: Circle) -> None:
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle: Rectangle) -> None:
        pass

    @abstractmethod
    def visit_triangle(self, triangle: Triangle) -> None:
        pass


class AreaCalculator(Visitor):
    def visit_circle(self, circle: Circle) -> None:
        print((circle.radius**2) * 3.14)

    def visit_rectangle(self, rectangle: Rectangle) -> None:
        print(rectangle.width * rectangle.height)

    def visit_triangle(self, triangle: Triangle) -> None:
        print(0.5 * triangle.base * triangle.height)


def client_code():
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=6)
    triangle = Triangle(base=3, height=4)

    area_calculator = AreaCalculator()

    circle.accept(area_calculator)
    rectangle.accept(area_calculator)
    triangle.accept(area_calculator)
