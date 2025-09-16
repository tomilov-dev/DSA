"""
Плохой пример: нарушение LSP — подкласс ломает ожидания клиента.
"""


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def set_width(self, width: int) -> None:
        self.width = width

    def set_height(self, height: int) -> None:
        self.height = height

    def area(self) -> int:
        return self.width * self.height


class Square(Rectangle):
    def set_width(self, width: int) -> None:
        self.width = width
        self.height = width  # Нарушение: меняет и ширину, и высоту

    def set_height(self, height: int) -> None:
        self.width = height  # Нарушение: меняет и ширину, и высоту
        self.height = height


def print_area(rect: Rectangle) -> None:
    rect.set_width(5)
    rect.set_height(10)
    print(f"Площадь: {rect.area()}")  # Ожидаем 5*10=50


def main():
    rect = Rectangle(2, 3)
    square = Square(2, 2)
    print_area(rect)  # Площадь: 50 (как ожидается)
    print_area(square)  # Площадь: 100 (неожиданно!)


if __name__ == "__main__":
    main()
