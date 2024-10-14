from abc import ABC
from abc import abstractmethod


class Graphic(ABC):
    @abstractmethod
    def draw(self) -> None:
        pass

    @abstractmethod
    def move(self, x: int, y: int) -> None:
        pass


class Circle(Graphic):
    def draw(self) -> None:
        print("Draw Circle")

    def move(self, x: int, y: int) -> None:
        print(f"Move Circle on ({x}, {y})")


class Square(Graphic):
    def draw(self) -> None:
        print("Draw Square")

    def move(self, x: int, y: int) -> None:
        print(f"Move Square on ({x}, {y})")


class Group(Graphic):
    def __init__(self) -> None:
        self.objects: list[Graphic] = []

    def add(self, object: Graphic) -> None:
        self.objects.append(object)

    def pop(self) -> Graphic:
        return self.objects.pop()

    def draw(self) -> None:
        for object in self.objects:
            object.draw()

    def move(self, x: int, y: int) -> None:
        for object in self.objects:
            object.move(x, y)


def client_code():
    # Пример использования
    circle1 = Circle()
    circle2 = Circle()
    square1 = Square()
    square2 = Square()

    group1 = Group()
    group1.add(circle1)
    group1.add(square1)

    group2 = Group()
    group2.add(circle2)
    group2.add(square2)
    group2.add(group1)

    group2.draw()
    group2.move(10, 20)
