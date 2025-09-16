"""
Хороший пример: соблюдение LSP — каждый класс ведёт себя предсказуемо.
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


class Square:
    def __init__(self, size: int) -> None:
        self.size = size

    def set_size(self, size: int) -> None:
        self.size = size

    def area(self) -> int:
        return self.size * self.size


def print_area(rect) -> None:
    if isinstance(rect, Rectangle):
        rect.set_width(5)
        rect.set_height(10)
    elif isinstance(rect, Square):
        rect.set_size(10)
    print(f"Площадь: {rect.area()}")


def main():
    rect = Rectangle(2, 3)
    square = Square(2)
    print_area(rect)  # Площадь: 50
    print_area(square)  # Площадь: 100


if __name__ == "__main__":
    main()
